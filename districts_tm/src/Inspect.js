import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';

function Inspect({MUid}) {

    const [mapiddemo, setmapiddemo] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const handleid = () => {
        if (MUid == '2021S051235191287'){
            return <p> Population: 200k
                Education average: Bachelors

            </p>
        }
        else if (MUid =='2021S051235190181'){
            return <p>
                Population: 100k
                Education average: Masters
            </p>

        }
        else {
            return <p> In progress.....</p>
        }
    }
    
  return (
    <div>
      <p> This is a Inspect Layer</p>
      {handleid()}
      
      <table>
        <thead>
            <tr>
                <th>Charact</th> 
                <th></th>
                <th></th>
                <th></th>
                <th>Value</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td> ages_0_to_4 </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_0_to_4')}</td>
                
            </tr>
            <tr>
                <td>ages_10_to_14</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_10_to_14')}</td>
                
            </tr>
            <tr>
                <td> ages_15_to_19 </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_15_to_19')}</td>
                
            </tr>
            <tr>
                <td>ages_20_to_24</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_20_to_24')}</td>
                
            </tr>
            <tr>
                <td> ages_25_to_29 </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_25_to_29')}</td>
                
            </tr>
            <tr>
                <td>ages_30_to_34</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_30_to_34')}</td>
                
            </tr>
            <tr>
                <td> ages_35_to_39 </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_35_to_39')}</td>
                
            </tr>
            <tr>
                <td>ages_40_to_44</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_40_to_44')}</td>
                
            </tr>
        </tbody>
      </table>
      
      {/* <p>the map id is {mapiddemo}</p> */}
      {/* <p> Map ID is {mapiddemo}</p> */}

    </div>
  )
}

export default Inspect
