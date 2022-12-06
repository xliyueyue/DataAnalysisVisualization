(function (func) {
    $.ajax({
        url: "/data/get_name",
        type: "GET",
        dataType: "json",
        success: function (data) {
            func(data);
        }
    });
})(function (data) {
    var html = "";
    data.series.forEach(function (item) {
        html += '<li><a href="javascript:;">' + item + '</a></li>'
    });
    var regBusiness = $("#regBusiness");
    //将后台的书放到regBusiness元素中
    regBusiness.html(html);
    textAdmin();
    function textAdmin() {
        try {
            //TagCanvas.Start:里面的内容直接从官网拷贝
            TagCanvas.Start('cloudCanvas', 'tags2', {
                fontSize: 20,
                textFont: "Arial, Helvetica, sans-serif",
                maxSpeed: 0.1,
                minSpeed: 0.01,
                textColour: '#41FDFE',
                textHeight: 12,
                outlineMethod: "colour",
                fadeIn: 800,
                outlineColour: "#41b1c3",
                outlineOffset: 0,
                depth: 0.97,
                minBrightness: 0.2,
                wheelZoom: false,
                reverse: true,
                shadowBlur: 2,
                shuffleTags: true,
                shadowOffset: [1, 1],
                stretchX: 1.2,
                initial: [0, 0.1],
                clickToFront: 600,
                outlineDashSpeed: 0.5,
                weight:true,
                weightMode:"both"

            });
        }
        catch (e) {
             // something went wrong, hide the canvas container
            var  c = document.getElementById('chart_5').style.display = 'none';
            var ctx=c.getContext("2d");
            ctx.font="30px Arial";

        }
    }
});