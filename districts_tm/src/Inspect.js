import React, { useEffect, useState } from 'react'

function Inspect({MUid}) {

    const [mapiddemo, setmapiddemo] = useState(null)
    
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
      
      {/* <p>the map id is {mapiddemo}</p> */}
      {/* <p> Map ID is {mapiddemo}</p> */}

    </div>
  )
}

export default Inspect
