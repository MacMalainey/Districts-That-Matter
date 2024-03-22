import React, { useEffect, useState } from 'react'
import axios, { all } from 'axios';

function Inspect({MUid}) {

    const [mapiddemo, setmapiddemo] = useState(null)
    const[demodata, setdemodata] = useState(null)
    const[charact, setcharact] = useState('')
    const handleCharact = (event) => {
        setcharact(event.target.value)
    }
  return (
    <div>
      
      
      <label>Select a Characteristic : </label>
      <select id='age' value={charact} onChange={handleCharact}>
            <option value='Placeholder'>---</option>
            <option value='Age'>Age</option>
            <option value='Birthplace'>Birthplace</option>
           
            <option value='Income'>Income</option>
            <option value='Density'>Density</option>
            <option value='Generation'>Generation</option>
            <option value='Household'>Houshold</option>
            <option value='Imigrated'>Imigrated</option>

      </select>

    {charact==='Age' && <table>
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
                <td> ages_5_to_9 </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_5_to_9')}</td>
                
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
            <tr>
                <td>ages_45_to_49</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_45_to_49')}</td>
                
            </tr>
            <tr>
                <td>ages_50_to_54</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_50_to_54')}</td>
                
            </tr>
            <tr>
                <td>ages_55_to_59</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_55_to_59')}</td>
                
            </tr>
            <tr>
                <td>ages_60_to_64</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_60_to_64')}</td>
                
            </tr>
            <tr>
                <td>ages_65_to_69</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_65_to_69')}</td>
                
            </tr>
            <tr>
                <td>ages_70_to_74</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_70_to_74')}</td>
                
            </tr>
            <tr>
                <td>ages_75_to_79</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_75_to_79')}</td>
                
            </tr>
            <tr>
                <td>ages_80_to_84</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_80_to_84')}</td>
                
            </tr>
            <tr>
                <td>ages_85_and_over</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('ages_85_and_over')}</td>
                
            </tr>
        </tbody>
      </table> }  
      
      {/* Birthplace */}
      {charact==='Birthplace' && <table>
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
                <td> birthplace_afghanistan </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_afghanistan')}</td>
                
            </tr>
            <tr>
                <td> birthplace_africa_other </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_africa_other')}</td>
                
            </tr>
            <tr>
                <td>birthplace_algeria</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_algeria')}</td>
                
            </tr>
            <tr>
                <td> birthplace_americas_other </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_americas_other')}</td>
                
            </tr>
            <tr>
                <td> birthplace_asia_other </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_asia_other')}</td>
                
            </tr>
            <tr>
                <td> birthplace_bangladesh </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_bangladesh')}</td>
                
            </tr>
            <tr>
                <td>birthplace_bosnia</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_bosnia')}</td>
                
            </tr>
            <tr>
                <td> birthplace_brazil </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_brazil')}</td>
                
            </tr>
            <tr>
                <td> birthplace_china </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_china')}</td>
                
            </tr>
            <tr>
                <td> birthplace_colombia </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_colombia')}</td>
                
            </tr>
            <tr>
                <td> birthplace_congo </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_congo')}</td>
                
            </tr>
            <tr>
                <td> birthplace_croatia </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_croatia')}</td>
                
            </tr>
            <tr>
                <td> birthplace_egypt </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_egypt')}</td>
                
            </tr>
            <tr>
                <td> birthplace_el_salvador </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_el_salvador')}</td>
                
            </tr>
            <tr>
                <td>birthplace_eritrea</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_eritrea')}</td>
                
            </tr>
            <tr>
                <td>birthplace_ethioopia</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_ethioopia')}</td>
                
            </tr>
            <tr>
                <td>birthplace_europe_other</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_europe_other')}</td>
                
            </tr>
            <tr>
                <td>birthplace_france</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('birthplace_france')}</td>
                
            </tr>
        </tbody>
      </table> }    
    
    {/* Income */}
    {charact==='Income' && <table>
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
                <td>income_under_5k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_under_5k')}</td>
                
            </tr>
            <tr>
                <td>income_from_5k_to_10k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_5k_to_10k')}</td>
                
            </tr>
            <tr>
                <td> income_from_10k_to_15k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_10k_to_15k')}</td>
                
            </tr>
            <tr>
                <td> income_from_15k_to_20k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_15k_to_20k')}</td>
                
            </tr>
            <tr>
                <td>income_from_20k_to_25k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_20k_to_25k')}</td>
                
            </tr>
            <tr>
                <td>income_from_25k_to_30k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_25k_to_30k')}</td>
                
            </tr>
            <tr>
                <td> income_from_30k_to_35k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_30k_to_35k')}</td>
                
            </tr>
            <tr>
                <td> income_from_35k_to_40k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_35k_to_40k')}</td>
                
            </tr>
            <tr>
                <td>income_from_40k_to_45k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_40k_to_45k')}</td>
                
            </tr>
            <tr>
                <td>income_from_45k_to_50k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_45k_to_50k')}</td>
                
            </tr>
            <tr>
                <td> income_from_50k_to_60k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_50k_to_60k')}</td>
                
            </tr>
            <tr>
                <td> income_from_60k_to_70k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_60k_to_70k')}</td>
                
            </tr>
            <tr>
                <td> income_from_70k_to_80k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_70k_to_80k')}</td>
                
            </tr>
            <tr>
                <td>income_from_80k_to_90k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_80k_to_90k')}</td>
                
            </tr>
            <tr>
                <td>income_from_90k_to_100k </td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_from_90k_to_100k')}</td>
                
            </tr>
            <tr>
                <td>income_income_from_100k_to_125k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_income_from_100k_to_125k')}</td>
                
            </tr>
            <tr>
                <td>income_income_from_125k_to_150k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_income_from_125k_to_150k')}</td>
                
            </tr>
            <tr>
                <td>income_income_from_150k_to_200k</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_income_from_150k_to_200k')}</td>
                
            </tr>
            <tr>
                <td>income_income_from_200k_and_over</td>
                <td></td>
                <td></td>
                <td></td>
                <td> {localStorage.getItem('income_income_from_200k_and_over')}</td>
                
            </tr>
           
        </tbody>
      </table> }    
    
    </div>
  )
}

export default Inspect
