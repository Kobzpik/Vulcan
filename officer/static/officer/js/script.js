Highcharts.chart('container', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Monthly total fine in 2022'
    },
    /*subtitle: {
        text: 'Source: <a href="http://en.wikipedia.org/wiki/List_of_cities_proper_by_population">Wikipedia</a>'
    },*/
    xAxis: {
        type: 'category',
        labels: {
            rotation: -45,
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Number of fine'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: 'fine : <b>{point.y:.1f} </b>'
    },
    series: [{
        name: 'Population',
        data: [
            ['January', 242],
            ['February', 208],
            ['March', 149],
            ['April', 137],
            ['May', 131],
            ['June', 127],
            ['July', 124],
            ['August', 122],
            ['September', 120],
            ['October', 117],
            ['November', 115],
            ['December', 112],
        ],
        dataLabels: {
            enabled: true,
            rotation: -90,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
                fontSize: '13px',
                fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
});

//pie chart
// Radialize the colors
Highcharts.setOptions({
    colors: Highcharts.map(Highcharts.getOptions().colors, function(color) {
        return {
            radialGradient: {
                cx: 0.5,
                cy: 0.3,
                r: 0.7
            },
            stops: [
                [0, color],
                [1, Highcharts.color(color).brighten(-0.3).get('rgb')] // darken
            ]
        };
    })
});

// Build the chart
Highcharts.chart('container1', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Fien categery according to nature of fine , 2022'
    },
    /*tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },*/
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                connectorColor: 'silver'
            }
        }
    },
    series: [{
        name: 'fine',
        data: [{
            name: 'offence1',
            y: 614
        }, {
            name: 'offence2',
            y: 1184
        }, {
            name: 'offence3',
            y: 1085
        }, {
            name: 'offence4',
            y: 467
        }, {
            name: 'offence6',
            y: 418
        }, {
            name: 'offence7',
            y: 705
        }]
    }]
});