!function ($) {
    jQuery(function () {
        // 页面加载时加载列表

        // 1. 获取笔记本信息
        $(function () {
            $.ajax({
                type: 'post',
                url: '/get_notebook/',
                success: function (str) { //返回json结果
                    data = JSON.parse(str); // 解析json字符串
                    // 成功和未登录都进行跳转
                    if (data.code == 1 || data.code == 20000) {
                        for (var i = 0; i < data.data.length; i++) {
                            $("#notebook_index").append(" <li class='li-style' value=" + data.data[i].id + "><span class='header-style'>" + data.data[i].name + "</span></li>");
                        }
                    } else {
                        alert(data.msg);
                    }
                },
                fail: function (err, status) {
                    console.log(err);
                }
            });
        });

    })


}(window.jQuery);


var add_note = function (obj) {
    $("#display").hide();
    $("#edit").show();
    window.location.href = "/new_note/";

};




