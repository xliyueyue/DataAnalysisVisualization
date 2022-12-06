(function (func) {
    $.ajax({
        url: "/data/get_grade_count",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById("chart_6"));

    var data1 =[];
    var data2 =[];
    $(data.series_data).each(function (k, v) {
        data1.push(v.grade);
        data2.push(v.count);

    });

    var option = {
        angleAxis: {
        },
        radiusAxis: {
            type: 'category',
            data: ['小学','初中','高中'],
            z: 10,
        },
        grid: [{
            top:40,
            left: 10,
        }],
        polar: {
        },
        series: [{
            type: 'bar',
            data: [513,730,990],
            axisLine: {onZero: true,
                            lineStyle:{
                    color:'#E0FFFF'
                }},
                axisLabel:{
                    textStyle:{
                        fontSize:12,
                        color:'#E0FFFF'
                    }
                },
            coordinateSystem: 'polar',
            name: '',
            stack: ''
        }],
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
});


