!function ($) {
    jQuery(function () {
        $("#commit_new_task").click(function (e) {
            var content = $("#task_content").val();
            var datas = {"content": content}
            $.ajax({
                type: 'POST',
                url: '/add_task/',
                data: datas,
                success: function (data) { //返回json结果
                    console.log(data);
                    if (data == "success") {
                        window.location.href = "/tasks/";
                    }

                    if (data == "none") {
                        alert("数据为空哦！");
                    }
                },
                fail: function (err, status) {
                    console.log(err)
                }
            });
        });


    })
}(window.jQuery);

