from typing import Any

import numpy as np
import pandas as pd
import geopandas as gpd

import shapely

from libpysal.weights import Queen, KNN
from sklearn.cluster import AgglomerativeClustering

def _interpret_z_score(z_score):
    if z_score <= -7:
        return "Insanely Lower"
    elif z_score <= -5:
        return "Extremely Lower"
    elif z_score <= -3:
        return "Signficantly Lower"
    elif z_score  <= -2:
        return " Notably Lower"
    elif z_score  <= -1:
        return "Marginally Lower"
    elif z_score  <= 0:
        return "No significant difference"
    elif z_score  <= 1:
        return "No significant difference"
    elif z_score  <= 2:
        return "Marginally Higher"
    elif z_score  <= 3:
        return "Notably Higher"
    elif z_score  <= 5:
        return "Signficantly Higher"
    elif z_score  <= 7:
        return "Extremely Higher"
    else:
        return "Insanely Higher"

class Processor:
    _data: gpd.GeoDataFrame
    _clusters: pd.DataFrame

    _ratios_labels: list[str]
    _reported_labels: list[str]
    _coi_aggregations: dict[str, Any]

    def __init__(self, data: pd.DataFrame, schema: dict[str, list[str]]):
        self._ratios_labels = []
        self._reported_labels = []
        self._coi_aggregations = {
            'dguid': lambda x: list(x),
            'population': 'sum',
            'landarea': 'mean',
            'density': 'mean'
        }
        self._clusters = None

        # The response count is recorded in an odd way for visible minority - N/A responses are not counted
        data["rc_visible_minority"] = data["rc_visible_minority"] + data["visible_minority_not_applicable"]
        for category, characteristcs in schema.items():
            rc_label = "rc_" + category
            for chr_label in characteristcs:
                ratio_label = chr_label+"_ratio"
                data = data.assign(**{ratio_label: data[chr_label] / data[rc_label] * 100})

                self._coi_aggregations[ratio_label] = 'mean'
                self._coi_aggregations[chr_label] = 'sum'

                self._ratios_labels.append(ratio_label)
                self._reported_labels.append(chr_label)

            self._coi_aggregations[rc_label] = 'sum'

            self._reported_labels.append(rc_label)

        data = data.assign(geometry=lambda x: shapely.from_wkt(x['geometry_wkt']))
        data.drop(columns=["geometry_wkt"], inplace=True)
        self._data = gpd.GeoDataFrame(data, crs="EPSG:4326", geometry="geometry")
        self._data.fillna(self._data[self._ratios_labels].mean(), inplace=True)

    def cluster(self, cached=True):
        if cached and self._clusters is not None:
            return self._clusters

        np.random.seed(0)

        # Compute model
        knn_weights = KNN.from_dataframe(self._data, k=4)
        model = AgglomerativeClustering(linkage="ward", n_clusters=10, connectivity=knn_weights.sparse, compute_distances=True)
        model.fit(self._data[self._ratios_labels])
        self._data["COI"] = model.labels_

        # Compute clusters
        self._clusters = self._data.dissolve(by='COI', aggfunc=self._coi_aggregations)

        # Determine "explanation"
        neighbor_weight_matrix = Queen.from_dataframe(self._clusters, use_index=True)
        self._clusters['explanation'] = pd.Series([None] * len(self._clusters))
        to_remove = []
        for index, row in self._clusters.iterrows():
            neighbor_rows = self._clusters.iloc[list(neighbor_weight_matrix[index].keys())]
            neighbor_rows = neighbor_rows[self._ratios_labels]
            neighbor_means = neighbor_rows.mean()
            neighbor_vars = neighbor_rows.std()
            z_scores = pd.Series(dtype=float)
            for col in self._ratios_labels:
                if neighbor_vars[col] == 0 or pd.isna(neighbor_vars[col]) or neighbor_vars[col] < 5:
                    neighbor_vars[col] = 5 #set 5% difference to be minimum one standard deviation
                z_scores[col] = (row[col] - neighbor_means[col]) / neighbor_vars[col]
            z_scores_abs = z_scores.abs()
            large_abs_z_scores = (z_scores_abs[z_scores_abs > 2])
            if large_abs_z_scores.count() == 0: # Not a significant difference... Remove
                to_remove.append(index)
                continue

            if large_abs_z_scores.count() == 1:
                largEST_abs_z_scores =  z_scores_abs.nlargest(2, keep='all')
                large_abs_z_scores = large_abs_z_scores.combine_first(largEST_abs_z_scores)

            explaination_dict = {}
            for attribute in large_abs_z_scores.index:
                explaination_dict[attribute.removesuffix('_ratio')] = {
                    'z_score': z_scores[attribute],
                    'ratio': row[attribute],
                    'total': row[attribute.removesuffix('_ratio')],
                    'neighbor_mean': neighbor_means[attribute],
                    'neighbor_var': neighbor_vars[attribute], 
                    'neighbor_vals': neighbor_rows[attribute].to_list(),
                    'interpretation': _interpret_z_score(z_scores[attribute])
                }
            self._clusters.at[index, 'explanation'] = explaination_dict

        self._clusters = self._clusters.drop(to_remove)
        return self._clusters

