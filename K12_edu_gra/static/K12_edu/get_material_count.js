(function (func) {
    $.ajax({
        url: "/data/get_material_count",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById("chart_7"));

    var option = {
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c}'
        },
        series: [
            {
                name: '漏斗图',
                type: 'funnel',
                width: '35%',
                height: '45%',
                left: '5%',
                top: '45%',
                funnelAlign: 'right',

                center: ['25%', '25%'],  // for pie

                data: data.series
            },
            {
                name: '金字塔',
                type: 'funnel',
                width: '35%',
                height: '45%',
                left: '5%',
                top: '0%',
                sort: 'ascending',
                funnelAlign: 'right',

                center: ['25%', '75%'],  // for pie

                data: data.series
            },
            {
                name: '漏斗图',
                type: 'funnel',
                width: '35%',
                height: '45%',
                left: '55%',
                top: '0%',
                funnelAlign: 'left',

                center: ['75%', '25%'],  // for pie

                data: data.series
            },
            {
                name: '金字塔',
                type: 'funnel',
                width: '35%',
                height: '45%',
                left: '55%',
                top: '45%',
                sort: 'ascending',
                funnelAlign: 'left',
                center: ['75%', '75%'],  // for pie
                data: data.series
            }
        ]
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
});


