// this component is capturing all required data and showing it on the map, be it for mapunits, coloring, erasing map units, seeing COI on the map,
// seeing gradient on the map as an overlayer 
// it fullfills FR 1, FR 2, FR 3, FR 4, FR 5, FR 8, FR 9, FR 10, FR 11, FR 12, FR 14, FR 15, FR 16, FR 17, FR 18, FR 19, FR 20, FR 21
import { Draw } from "leaflet"
import React, { useContext, useEffect, useState } from "react"
import 'leaflet/dist/leaflet.css';
import { MapContainer, TileLayer, Polyline, GeoJSON, LayersControl, Marker, Popup } from 'react-leaflet';


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
    
    const { data: districtData, callback: districtCallback } = useContext(DistrictsContext);
    const { data: gradientSelect, callback: setGradientSelect, category: expectedcategory} = useContext(GradientSelectContext);
    const { data: mapMode, callback: _ } = useContext(MapModeContext);
    const {data: showcoionmap} = useContext(COISelectContext)
    const center = [43.65107, - 79.347015];
    const [selectedmapunitid, setselectedmapunitid] = useState(null); // FR9
    const [selectedCOI, setselectedCOI] = useState(null)
    const [selectedCOIdata, setselectedCOIdata] = useState(null)
    
    let baseStyle = { fillColor: 'transparent', color: 'grey', weight: 0.5 };
    //fulfills FR 10

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
    
    //FUlfills FR 16, FR 17, FR 18, FR21
    const colormapunit = (mapunit) => {
      
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
                        // console.log("COIotherarray:", COIotherarray)
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

    // return handles plotting of map units as the base layer
    // it plots another layer for user to color/erase map units
    // it plots COI data as another layer (checks for user selection of showonmap) and allowing user to click on a COI to check for explanation for that map unit
    // the explanation takes a second to load 
    // it plots gradient overlay on the map using the required data ( checks for user selection to show on map)
    // fullfills FR 1-4, FR 8, FR 9, FR 10, FR 11, FR 12
    // fullfills FR 14 
    //fullfills FR 16,FR17,FR18, FR19, FR20, FR 21
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