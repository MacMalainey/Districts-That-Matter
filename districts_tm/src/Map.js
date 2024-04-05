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
import { colors } from './config';
import { MapUnitsAllContext, COIContext, DistrictsContext, GradientSelectContext } from "./App";
import { ViewAges, ViewPopulation } from "./GradientViews";

// FR1: Map Render
// FR2: Map Fetch
// FR3: Map.Units.Render
// FR4: Map.Units.Fetch
// FR5: Map.Navigate
let COIarray = [];
let Visualarray = [];

localStorage.setItem('coloractive', '')
localStorage.setItem('mapid', '')
localStorage.setItem('colorid', '')
localStorage.setItem('COIexp', '')
let COIotherarray = [];
function DrawMap() {
  const mapData = useContext(MapUnitsAllContext);
  const coiData = useContext(COIContext);
  const { data: districtData, callback: districtCallback } = useContext(DistrictsContext);
  const { data: gradientSelect, callback: setGradientSelect } = useContext(GradientSelectContext);

  const center = [43.65107, - 79.347015];
  const [changes, setChanges] = useState({});
  const [selectedmapunit, setselectedmapunit] = useState(null);
  const [selectedmapunitid, setselectedmapunitid] = useState(null);
  const [coida, setcoida] = useState(null)
  const [dguid, setdguid] = useState(15)
  const [coloractiveid, setcoloract] = useState(null)
  useEffect(() => {
    setcoloract(localStorage.getItem('coloractive'))
  })
  // const coloractiveid = localStorage.getItem('coloractive')
  const colid = localStorage.getItem('colorid')
  const cursorid = localStorage.getItem('cursor')
  const eraseractiveid = localStorage.getItem('eraser')
  const [selectedCOI, setselectedCOI] = useState(null)
  const [selectedCOIdata, setselectedCOIdata] = useState(null)

  const showCOIonmap = localStorage.getItem('showcoionmap')

  let baseStyle = { fillColor: 'transparent', color: 'grey', weight: 0.5 };
  if (gradientSelect != null) {
    baseStyle = (mapunit) => ViewPopulation(mapunit, gradientSelect)
  }

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
  //  this gets the mapid only after its set
  useEffect(() => {
    if (selectedmapunitid != null) {
      localStorage.setItem('mapid', selectedmapunitid)
      console.log("selected map unit is: ", selectedmapunitid)
      definedistrict(selectedmapunitid, colid)
    }


  }, [selectedmapunitid])

  // this function checks for dguids and color id, if the id is non 100, it sends both values otherwise it sends a null as in erase 

  const definedistrict = (val1, val2) => {
    console.log("hello us", val1)

    try {



      if (val2 == 100) {

        changes[val1] = null
      }
      else {
        changes[val1] = parseInt(val2)
      }
      setChanges(changes)

    }

    catch {
      console.log("Cant recieve id's on time")
    }

  }





  return (

    <div className="map">



      <MapContainer center={center} zoom={10} style={{ height: '1000px' }}>
        <TileLayer

          url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png"

        />
        <LayersControl postition='topright'>
          <LayersControl.BaseLayer name='Baselayer' checked='Baselayer'>
            {mapData && <GeoJSON data={mapData} style={baseStyle} eventHandlers={{ click: (e) => { setselectedmapunitid(e.layer.feature.id) } }} />}

          </LayersControl.BaseLayer>




        </LayersControl>


        {coiData && showCOIonmap == 1 && <GeoJSON data={coiData} style={{ fillColor: 'red', color: 'black', weight: 2, fillOpacity: 0.6 }} eventHandlers={{
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

        {mapData && coloractiveid == 1 && <GeoJSON data={mapData} style={colormapunit} eventHandlers={{
          click: (e) => {
            setselectedmapunit(e.layer.feature);
            { console.log(e.layer.feature.id) }
            let cid = localStorage.getItem('colorid')
            if (cid == 100) {
              cid = null
            }
            districtData[e.layer.feature.id] = cid
            districtCallback(districtData)
            setselectedmapunitid(e.layer.feature.id);
          }
        }} />}

        {/* {gradientSelect && <GeoJSON data={mapData} style={(mapunit) => ViewPopulation(mapunit, gradientSelect)} />} */}
        {localStorage.setItem('defineddistricts', JSON.stringify(changes))}

      </MapContainer>

    </div>



  );


}

export default DrawMap