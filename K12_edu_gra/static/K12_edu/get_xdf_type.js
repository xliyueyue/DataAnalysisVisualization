(function (func) {
    $.ajax({
        url: "/data/get_xdf_type",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var myChart = echarts.init(document.getElementById("chart_2"));

    var data1 =[];
    var data2 =[];
    var data3 =[];
    $(data.series_data).each(function (k, v) {
        data1.push(v.type);
        data2.push(v.price);
        data3.push(v.count);
    });

    var option = {
        title: {
            text: '',
            subtext: '',
            left: 'center'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                animation: false
            }
        },

        axisPointer: {
            link: {xAxisIndex: 'all'}
        },

        grid: [{
            top: 35,
            left: 50,
            right: 20,
            height: '35%'
        }, {
            left: 50,
            right: 20,
            top: '50%',
            height: '40%'
        }],
        xAxis: [
            {
                type: 'category',
                boundaryGap: false,
                axisLine: {onZero: true,
                            lineStyle:{
                    color:'#B0C4DE'
                }},
                axisLabel:{
                    textStyle:{
                        fontSize:12.75
                    }

                },
                data: data1
            },
            {
                gridIndex: 1,
                type: 'category',
                boundaryGap: false,
                axisLine: {onZero: true,
                            lineStyle:{
                    color:'#B0C4DE'
                }},
                axisLabel:{
                    textStyle:{
                        fontSize:12.75
                    }

                },
                data: data1,
                position: 'top'
            },
        ],
        yAxis: [
            {
                name: '报名量',
                nameTextStyle:{fontSize:17},
                type: 'value',
                axisLine:{
                    lineStyle:{
                        color:'#B0C4DE'
                    }
            },
                axisLabel:{
                    textStyle:{
                        fontSize:15
                    }

                },
                max: 2500
            },
            {
                gridIndex: 1,
                name: '课时单价',
                nameTextStyle:{fontSize:17},
                type: 'value',
                axisLine:{
                    lineStyle:{
                        color:'#B0C4DE'
                    }
            },
                axisLabel:{
                    textStyle:{
                        fontSize:15
                    }

                },
                inverse: true
            }
        ],
        series: [
            {
                name: '报名量',
                type: 'line',
                symbolSize: 8,
                hoverAnimation: false,
                data: data3
            },
            {
                name: '课时单价',
                type: 'line',
                xAxisIndex: 1,
                yAxisIndex: 1,
                symbolSize: 8,
                hoverAnimation: false,
                itemStyle: {
				normal: {
					color: '#B22222', //改变折线点的颜色
					lineStyle: {
						color: '#FFA500' //改变折线颜色
					}

			},

                },
                data: data2
            }
        ]
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
});

