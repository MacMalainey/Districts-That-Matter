import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState, createContext } from 'react';
import DrawMap from './Map';
import Sidebar from './Sidebar';
import axios from 'axios';
import { MAP_MODE_HAND } from './config';
import { callback } from 'chart.js/helpers';
// import DataLayer from './DataLayer';
// import Inspect from './Inspect';

export const MapUnitsAllContext = createContext(null);
export const MapUnitDemoContext = createContext(null);
export const COIContext = createContext(null);
export const SchemaContext = createContext(null);
export const DistrictsContext = createContext(null);
export const GradientSelectContext = createContext(null);
export const MapModeContext = createContext(null);
export const MapUnitsAllCategoryApiContext = createContext(null);
export const COISelectContext = createContext(null)
export const EvaluationContext = createContext(null)
export const EvaluationPopContext = createContext(null)
export const EvaluationOtherContext = createContext(null)
async function MapUnitsAllApi(onUpdate) {
  const response = await axios.get('http://127.0.0.1:5000/api/units/all', {
   
  })
  onUpdate(response.data)
  
}
  
async function MapUnitsAllCategoryApi(onUpdate, category) {
  if(category!=null){
    const response = await axios.get('http://127.0.0.1:5000/api/units/category/' + category)
    onUpdate(response.data)
    
  }
  
}

async function Evaluation(onUpdate){
   
      
      const response = await axios.get('http://127.0.0.1:5000/api/districts/demographics')
      onUpdate(response.data)
      

}



async function COIApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/cois/all')
  onUpdate(response.data)
}

async function DistrictsContextApi(onUpdate, category) {
  const response = await axios.get('http://127.0.0.1:5000/api/districts')
  onUpdate(response.data)
}

let category = null;

let expectedCategory = null;

function App() {
  const [COIData, setCOIData] = useState(null);
  const [mapUnitData, setMapUnitData] = useState(null);
  const [districtData, setDistrictData] = useState(null);
  const [gradientSelect, setGradientSelect] = useState(null);
  const [mapMode, setMapMode] = useState(MAP_MODE_HAND);
  const [categoryData, setcategoryData] = useState(null);
  const [showcoionmap, setshowcoionmap] = useState(false)
  const [Evaluationdata, setEvaluationdata] = useState(null)
  const [showpop, setshowpop] = useState(false)
  const [showother, setshowother] = useState(false)
  
  useEffect(() => {
    MapUnitsAllApi(setMapUnitData)
    
  }, []);

  useEffect(() => {
    
    Evaluation(setEvaluationdata)
    
  }, []);
  
  useEffect(() => {
    MapUnitsAllCategoryApi(setcategoryData, expectedCategory)
    category = expectedCategory
  }, [expectedCategory]);
  useEffect(() => {
    COIApi(setCOIData)
  }, []);

  useEffect(() => {
    DistrictsContextApi(setDistrictData)
  }, []);
  return (
    <div className='container'>
      <MapUnitsAllContext.Provider value={{data:mapUnitData}}>
        <COIContext.Provider value={COIData}>
            <DistrictsContext.Provider value={{data: districtData, callback: setDistrictData}}>
             <MapUnitsAllCategoryApiContext.Provider value = {{data: categoryData, category:category}}>
               <GradientSelectContext.Provider value={{
                  data: gradientSelect,
                  callback: (data) => {
                    if (data != null && data != "population" && data != "landarea" ) {
                      expectedCategory = (data.split('_'))[0]
                      if(expectedCategory == "visible"){
                        expectedCategory = "visible_minority"
                      }

                    }
                    setGradientSelect(data);
                    
                  },
                  category: expectedCategory
                  }}>
                  <MapModeContext.Provider value = {{data: mapMode, callback: setMapMode}}>
                    <COISelectContext.Provider value={{data:showcoionmap, callback: setshowcoionmap}}>
                        <DrawMap/>
                      <EvaluationContext.Provider value={Evaluationdata}>
                        <EvaluationPopContext.Provider value = {{data:showpop, callback:setshowpop}}>
                          <EvaluationOtherContext.Provider value = {{data:showother, callback:setshowother}}>
                   
                                
                                <Sidebar/>

                          </EvaluationOtherContext.Provider>
                        </EvaluationPopContext.Provider>
                      </EvaluationContext.Provider>
                    </COISelectContext.Provider>
                  </MapModeContext.Provider>
               </GradientSelectContext.Provider>
              </MapUnitsAllCategoryApiContext.Provider>
            </DistrictsContext.Provider>
        </COIContext.Provider>
      </MapUnitsAllContext.Provider>
    </div>
  );
}

export default App;
