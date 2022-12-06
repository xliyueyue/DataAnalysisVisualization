(function (func) {
    $.ajax({
        url: "/data/get_all",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById("chart_3"));

    var data1 =[];
    var data2 =[];
    var data3 =[];
    $(data.series_data).each(function (k, v) {
        data1.push(v.course);
        data2.push(v.price);
        data3.push(v.count);
    });

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
                crossStyle: {
                    color: '#999'
                }
            }
        },
        grid: [{
            top:40,
            bottom: 20,
            left: 70,
            right: 30,
            height: '80%'
        }],
        xAxis: [
            {
                type: 'category',
                axisLine: {onZero: true,
                            lineStyle:{
                    color:'#B0C4DE'
                }},
                axisLabel:{
                    textStyle:{
                        fontSize:12
                    }

                },
                data: data1,
                axisPointer: {
                    type: 'shadow'
                }
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: '价格',
                nameTextStyle:{fontSize:13},
                min: 0,
                max: 6000,
                interval: 1000,
                axisLine: {onZero: true,
                            lineStyle:{
                    color:'#B0C4DE'
                }},
                axisLabel:{
                    formatter: '{value}￥',
                    textStyle:{
                        fontSize:13
                    }

                }
            },
            {
                type: 'value',
                name: '数量',
                nameTextStyle:{fontSize:13},
                min: 0,
                max: 600,
                interval: 100,
                axisLine: {onZero: true,
                            lineStyle:{
                    color:'#B0C4DE'
                }},
                axisLabel:{
                    formatter: '{value}￥',
                    textStyle:{
                        fontSize:13
                    }

                }
            }
        ],
        series: [
            {
                name: '价格',
                type: 'bar',
                data: data2
            },

            {
                name: '数量',
                type: 'line',
                yAxisIndex: 1,
                itemStyle: {
				normal: {
					color: 'write', //改变折线点的颜色
					lineStyle: {
						color: '#FFFF99' //改变折线颜色
					}

			},

                },
                data: data3
            }
        ]
    };

     myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
});
