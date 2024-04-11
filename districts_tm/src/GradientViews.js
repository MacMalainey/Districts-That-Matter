// this function is handling the gradient for each category
// it calculated the % by taking in the actual value of that category and dividing it with the registered count to keep gradient range consistent
// the gradient range  for all category is 
//1)	If % < 14.9 -> color: #D3D3D3
// 2)	If % >= 14.9 but < 29.9 -> color: #C0C0C0
// 3)	If % >= 29.9 but < 44.9 -> color : #DCDCDC
// 4)	If % >= 44.9 but < 59.9 -> color: #808080
// 5)	If % >= 59.9 but <74.9 -> color: #696969
// 6)	If % >= 74.9 but < 89.9 -> color: #A9A9A9
// 7)	Otherwise return -> color: #444444


export const ViewAges = (mapunit, value) => {
    const testage = mapunit[value]
    const testrc = mapunit['rc_ages']
    const result = (testage / testrc) * 100
   
    if (result < 14.9) {
        return {
            fillColor: '#D3D3D3',

            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }

    else if (result > 15 && result < 29.9) {
        return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 30 && result < 44.9) {
        return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 45 && result < 59.9) {
        return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 60 && result < 74.9) {
        return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 75 && result < 89.9) {
        return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else {
        return {
            fillColor: '#444444',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }

}

export const ViewIncome = (mapunit, value) => {

    // console.log("Demag kharab part 2", VOincome)
    const testincome = mapunit[value]
    const testrc = mapunit['rc_income']
    const result = (testincome / testrc) * 100
    
    if (result < 14.9) {
        return {
            fillColor: '#D3D3D3',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 15 && result < 29.9) {
        return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 30 && result < 44.9) {
        return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 45 && result < 59.9) {
        return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 60 && result < 74.9) {
        return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 75 && result < 89.9) {
        return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else {
        return {
            fillColor: '#444444',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }

}

export const ViewVisibleM = (mapunit, value) => {

    // console.log("Demag kharab part 2", VOincome)
    const testvisibleM = mapunit[value]
    const testrc = mapunit['rc_visible_minority']
    const result = (testvisibleM / testrc) * 100
    
    if (result < 14.9) {
        return {
            fillColor: '#D3D3D3',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 15 && result < 29.9) {
        return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 30 && result < 44.9) {
        return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 45 && result < 59.9) {
        return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 60 && result < 74.9) {
        return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 75 && result < 89.9) {
        return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else {
        return {
            fillColor: '#444444',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }

}


export const ViewBirthplace = (mapunit, value) => {

    // console.log("Demag kharab part 2", VOincome)
    const testbirthplace = mapunit[value]
    const testrc = mapunit['rc_birthplace']
    const result = (testbirthplace / testrc) * 100
    
    if (result < 14.9) {
        return {
            fillColor: '#D3D3D3',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 15 && result < 29.9) {
        return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 30 && result < 44.9) {
        return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 45 && result < 59.9) {
        return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 60 && result < 74.9) {
        return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result > 75 && result < 89.9) {
        return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else {
        return {
            fillColor: '#444444',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
}


export const ViewPopulation = (mapunit, _) => {

    // const testpop = mapunit.properties["population"]
    const testrc_pop = 29669
    const result = (mapunit / testrc_pop) * 100
    if (result < 14.9) {
        return {
            fillColor: '#D3D3D3',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result >= 14.9 && result < 29.9) {

        return {
            fillColor: '#C0C0C0',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result >= 29.9 && result < 44.9) {

        return {
            fillColor: '#DCDCDC',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result >= 44.9 && result < 59.9) {

        return {
            fillColor: '#808080',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result >= 59.9 && result < 74.9) {

        return {
            fillColor: '#696969',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else if (result >= 74.9 && result < 89.9) {

        return {
            fillColor: '#A9A9A9',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }
    else {
        return {
            fillColor: '#444444',
            color: 'lightgrey',
            weight: 0.5,
            fillOpacity: 0.3,

        };
    }

}