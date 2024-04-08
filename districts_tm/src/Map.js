import { Draw } from "leaflet"
import React, { useContext, useEffect, useState } from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON, LayersControl, Marker, Popup } from 'react-leaflet';
import TestPoly from "./TestGeo";
import L from 'leaflet';
import './Map.css';
import axios from 'axios';
import Sidebar from "./Sidebar";
import { eventWrapper } from "@testing-library/user-event/dist/utils";
import { BsBox } from "react-icons/bs";
import { MAP_MODE_ERASE, MAP_MODE_PAINT, colors } from './config';
import { MapUnitsAllContext, COIContext, DistrictsContext, GradientSelectContext, MapModeContext, MapUnitsAllCategoryApiContext, COISelectContext} from "./App";
import { ViewAges, ViewPopulation, ViewIncome, ViewBirthplace, ViewVisibleM} from "./GradientViews";
import { GrAid } from "react-icons/gr";

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
let COIarray = [];  

localStorage.setItem('coloractive', '')
localStorage.setItem('mapid', '')
localStorage.setItem('colorid', '')
localStorage.setItem('COIexp', '')
let COIotherarray = [];
function DrawMap() {
    const {data: CategoryData, category:category} = useContext(MapUnitsAllCategoryApiContext)
    const {data: mapData} = useContext(MapUnitsAllContext);
    const coiData = useContext(COIContext);
    console.log("COI check", coiData)
    const { data: districtData, callback: districtCallback } = useContext(DistrictsContext);
    const { data: gradientSelect, callback: setGradientSelect, category: expectedcategory} = useContext(GradientSelectContext);
    const { data: mapMode, callback: _ } = useContext(MapModeContext);
    const {data: showcoionmap} = useContext(COISelectContext)
    const center = [43.65107, - 79.347015];
    const [selectedmapunitid, setselectedmapunitid] = useState(null);
    const [selectedCOI, setselectedCOI] = useState(null)
    const [selectedCOIdata, setselectedCOIdata] = useState(null)
    console.log("Category Data", CategoryData)
    let baseStyle = { fillColor: 'transparent', color: 'grey', weight: 0.5 };
    
    if(gradientSelect != null && (gradientSelect == "population" || gradientSelect == "landarea" || category == expectedcategory)) {
      
      if (gradientSelect == "population") {
      
        baseStyle = (mapunit) => ViewPopulation(mapunit.properties.population,gradientSelect)
      }
      else if (expectedcategory == "income") {
        baseStyle = (mapunit) => ViewIncome(CategoryData[mapunit.id], gradientSelect)
      }
      else if (expectedcategory =="ages") {
        baseStyle = (mapunit) => ViewAges(CategoryData[mapunit.id], gradientSelect)
      }
      else if (expectedcategory =="birthplace") {
        baseStyle = (mapunit) => ViewBirthplace(CategoryData[mapunit.id], gradientSelect)
      }
      else if (expectedcategory =="visible_minority") {
        baseStyle = (mapunit) => ViewVisibleM(CategoryData[mapunit.id], gradientSelect)
      }
    }
    

    const colormapunit = (mapunit) => {
      console.log("hello from color:", mapunit)
        const base = {
            fillOpacity: 0,
            weight: 0.5
        };

        const did = districtData[mapunit.id];
        if (did != undefined || did != null) {
            base['fillOpacity'] = 0.6;
            base['fillColor'] = colors[did - 11]
        }
        return base
    };


    // handle COI data for selected COI, except explanation, which is handled separately. 
    useEffect(() => {
        const handleCOIother = () => {
            COIotherarray = []
            try {
                if (COIotherarray.length != 132) {


                    for (const tempdata in selectedCOIdata) {
                        // console.log(tempdata,selectedCOIdata)
                        const tempval = selectedCOIdata[tempdata]
                        // console.log("interpretation of {} this item is", reason, ite.interpretation)
                        // COIotherarray.push([tempdata, tempval])
                        COIotherarray.push([tempdata, tempval])
                        console.log("COIotherarray:", COIotherarray)
                        localStorage.setItem('COIotherarray', JSON.stringify(COIotherarray))
                        // localStorage.setItem('COIexp', JSON.stringify(COIarray))

                    }
                }
            }
            catch {
                console.log("Error with COI explanation parsing......")
            }

            COIarray = [] // clear array after storage, otherwise it will append to the existing array. 
        }
        //  console.log("selected COI explanation is:", selectedCOI.generation_first.interpretation)
        handleCOIother();


    }, [selectedCOIdata])

    return (

        <div className="map">



            <MapContainer center={center} zoom={10} style={{ height: '1000px' }}>
                <TileLayer

                    url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"

                />
                <LayersControl postition='topright'>
                    <LayersControl.BaseLayer name='Baselayer' checked='Baselayer'>
                        {mapData && <GeoJSON data={mapData} style={baseStyle} eventHandlers={{ click: (e) => { setselectedmapunitid(e.layer.feature.id) 
                        
                        localStorage.setItem('mapid', e.layer.feature.id)
                        } }} />}
                          
                    </LayersControl.BaseLayer>




                </LayersControl>

                {coiData && showcoionmap==true && <GeoJSON data={coiData} style={{ fillColor: 'red', color: 'black', weight: 2, fillOpacity: 0.6 }} eventHandlers={{
                    click: (e) => {
                        setselectedCOI(e.layer.feature.properties.explanation);


                        setselectedCOIdata(e.layer.feature.properties)
                        COIarray = []
                        for (const reason in selectedCOI) {
                            const ite = selectedCOI[reason]
                            // console.log("interpretation of {} this item is", reason, ite.interpretation)
                            COIarray.push([reason, ite.interpretation])


                        }
                    }
                }}
                >
                    <Popup>
                        <p>
                            <h4>Explanation</h4>
                            <p>
                                <ul>
                                    {COIarray.map((charact, indexvalue) => (
                                        <li key={indexvalue} ><strong>{charact[0]}</strong> : {charact[1]}</li>
                                    ))}

                                </ul>

                            </p>

                        </p>
                    </Popup>
                </GeoJSON>}

                {mapData && (mapMode == MAP_MODE_PAINT || mapMode == MAP_MODE_ERASE) && <GeoJSON data={mapData} style={colormapunit} eventHandlers={{
                    click: (e) => {
                        let cid = localStorage.getItem('colorid')
                        if (cid == 100 || mapMode == MAP_MODE_ERASE) {
                            cid = null
                        }
                        districtData[e.layer.feature.id] = cid
                        districtCallback(districtData)
                        setselectedmapunitid(e.layer.feature.id);
                        
                    }
                }} />}

            </MapContainer>

        </div>



    );


}

export default DrawMap