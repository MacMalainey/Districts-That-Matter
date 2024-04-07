export const ViewAges = (mapunit, value) => {
    const testage = mapunit.properties[value]
    const testrc = mapunit.properties['rc_ages']
    const result = (testage / testrc) * 100
   console.log("GV", mapunit)
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
    const testincome = mapunit.properties[value]
    const testrc = mapunit.properties['rc_income']
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
    const testvisibleM = mapunit.properties[value]
    const testrc = mapunit.properties['rc_visible_minority']
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
    const testbirthplace = mapunit.properties[value]
    const testrc = mapunit.properties['rc_birthplace']
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

    const testpop = mapunit.properties["population"]
    const testrc_pop = 29669
    const result = (testpop / testrc_pop) * 100
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