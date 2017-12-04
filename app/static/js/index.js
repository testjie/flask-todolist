!function ($) {
    jQuery(function () {
        $("#login").click(function (e) {
            $("#signin_modal").modal("show");
            e.preventDefault()
        });

        $("#reg").click(function (e) {
            $("#signup_modal").modal("show");
            e.preventDefault()
        });

        $("#goto_reg").click(function (e) {
            $("#signin_modal").modal("hide");
            $("#signup_modal").modal("show");
            e.preventDefault()
        });


        $("#togo_login").click(function (e) {
            $("#signup_modal").modal("hide");
            $("#signin_modal").modal("show");
            e.preventDefault()
        });

    })
}(window.jQuery);


// 激活task
var active_task = function (obj) {
    if (confirm("是否继续")) {
        // 删除操作
        var datas = {"id": obj.name};
        $.ajax({
            type: 'post',
            url: '/active_task/',
            data: datas,
            success: function (str) { //返回json结果
                data = JSON.parse(str); // 解析json字符串
                // 成功和未登录都进行跳转
                if (data.code == 1 || data.code == 20000) {
                    if (data.url != "") {
                        window.location.href = "/";
                    }
                } else {
                    alert(data.msg);
                }

            },
            fail: function (err, status) {
                console.log(err);
            }
        });
    }
};

// 关闭task
var finish_task = function (obj) {
    if (confirm("是否继续")) {
        // 删除操作
        var datas = {"id": obj.name};
        $.ajax({
            type: 'post',
            url: '/finish_task/',
            data: datas,
            success: function (str) { //返回json结果
                data = JSON.parse(str); // 解析json字符串
                // 成功和未登录都进行跳转
                if (data.code == 1 || data.code == 20000) {
                    if (data.url != "") {
                        window.location.href = "/";
                    }
                } else {
                    alert(data.msg);
                }

            },
            fail: function (err, status) {
                console.log(err);
            }
        });
    }
};


