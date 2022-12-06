(function (func) {
    $.ajax({
        url: "/data/get_grade_price",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById("chart_4"));

    var option = {
        tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
        },
        calculable: true,
        series: [

            {
                name: '年级费用',
                type: 'pie',
                radius: [10, 160],
                roseType: 'area',
                x: '50%',               // for funnel
                max: 30,                // for funnel
                sort: 'ascending',     // for funnel
                data: data.series
            }
        ]
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
});


