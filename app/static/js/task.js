!function ($) {
    jQuery(function () {
        // 页面加载时加载列表
        $(function () {
            tasklist(1);
        });


        // 新增
        $("#commit_new_task").click(function (e) {
            var content = $("#task_content").val();
            var datas = {"content": content};
            $.ajax({
                type: 'post',
                url: '/add_task/',
                data: datas,
                success: function (str) { //返回json结果
                    data = JSON.parse(str); // 解析json字符串
                    if (data.code == 1) {
                        window.location.href = data.url;
                    } else {
                        alert(data.msg)
                    }
                },
                fail: function (err, status) {
                    console.log(err)
                }
            });
        });

        // 修改
        $("#update_task_but").click(function (e) {

            var datas = {};
            datas["id"] = $("#task_id_getter").val();
            datas["title"] = $("#task_content1").val();
            datas["status"] = $("#task_status_update").find("option:selected").val();

            $.ajax({
                type: 'post',
                url: '/update_task/',
                data: datas,
                success: function (str) { //返回json结果
                    data = JSON.parse(str); // 解析json字符串
                    if (data.code == 1 || data.code == 20000) {
                        window.location.href = data.url;
                    } else {
                        alert(data.msg)
                    }
                },
                fail: function (err, status) {
                    console.log(err)
                }
            });
        });


        // 设置全部选中，或者全部取消
        $("#all_checkbox").click(function (e) {
            var attrs = $("input[name=checkbox]");
            for (var i = 0; i < attrs.length; i++) {
                if ($('input[name="all_checkbox"]')[0].checked) {
                    attrs[i].checked = true;
                } else {
                    attrs[i].checked = false;
                }
            }
        });

        // 删除
        $("#del_task").click(function (e) {
            if (confirm("是否继续")) {
                var ids = "";
                var attrs = $("input[name=checkbox]");
                //遍历获取id并添加value
                for (var i = 0; i < attrs.length; i++) {
                    if (attrs[i].checked == true) {
                        ids = ids + "," + attrs[i].value;
                    }
                }

                var datas = {"ids": ids};

                $.ajax({
                    type: 'post',
                    url: '/del_task/',
                    data: datas,
                    success: function (str) { //返回json结果
                        data = JSON.parse(str); // 解析json字符串
                        // 成功和未登录都进行跳转
                        if (data.code == 1 || data.code == 20000) {
                            if (data.url != "") {
                                window.location.href = data.url;
                            }
                        } else {
                            alert(data.msg);
                        }

                    },
                    fail: function (err, status) {
                        console.log(err)
                    }
                });
            }
        });


        // 渲染task_table
        var tasklist = function (page) {
            // 获取信息
            $.ajax({
                type: 'post',
                url: '/get_tasks/',
                data: {"page": page},
                success: function (str) { //返回json结果
                    data = JSON.parse(str); // 解析json字符串
                    if (data.code == 1) {

                        // 渲染模板
                        $.each(data.data.datas, function (n, value) {
                            //alert(data.data.datas);
                            var trs = "";
                            var tbody = "";

                            var id = value["id"];
                            var title = value["title"];
                            var createTime = value["create_time"];

                            //动态输出状态和激活/完成按钮
                            var status;
                            var done_button;
                            if (value["status"] == "1") {
                                status = "未完成";
                                done_buuton = "<button class='am-btn am-btn-default am-btn-xs am-hide-sm-only' type='button' onclick='finish_task(this)' name='" + id + "'>" +
                                    "<span class='am-icon-lock'></span> 完成</button>";

                            } else {
                                status = "已完成";
                                done_buuton = "<button class='am-btn am-btn-default am-btn-xs am-hide-sm-only' type='button' onclick='active_task(this)' name='" + id + "'>" +
                                    "<span class='am-icon-repeat'></span> 激活</button>";
                            }
                            trs += "<tr><td><input type='checkbox' name='checkbox' value='" + id + "'/></td><td>" + id + "</td>" +
                                "<td><a href='#' id ='title" + id + "'>" + title + "</a></td><td id='status" + id + "'>" + status + "</td>" +
                                "<td class='am-hide-sm-only'>" + createTime + "</td>" +
                                "<td><div class='am-btn-toolbar'><div class='am-btn-group am-btn-group-xs'><button class='am-btn am-btn-default am-btn-xs am-text-secondary' type='button' onclick='edit_task(this)' name ='" + id + "'><span class='am-icon-pencil-square-o' ></span> 编辑</button>" + done_buuton + "<button type='button' id='" + id + "' onclick='delete_task(this);' class='am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only'><span class='am-icon-trash-o' ></span> 删除</button></div></div></td></tr>";

                            tbody += trs;
                            $("#task_table").append(tbody);
                        });

                        // 渲染翻页
                        $("#total_page").html(data.data.page_info["page_total"]);
                        var last_one = data.data.page_info["page_no"];
                        var lis = "<li><a href='javascript:;' id='pre_page'onclick='tasklist1(\"pre\")'>«</a></li>";
                        var next = "<li><a href='javascript:;' id='next_page' onclick='tasklist1(\"last\")' name='" + last_one + "'>»</a></li>";

                        //遍历li
                        for (var i = 0; i < last_one; i++) {
                            var current = i + 1;
                            //如果是当前页，则渲染为激活状态，否则就不是当前页
                            if (page == current) {
                                lis += "<li class='am-active'><a href='javascript:;' id='current_page' onclick='tasklist1(" + current + ")'>" + current + "</a></li>";
                            } else {
                                lis += "<li><a href='javascript:;' onclick='tasklist1(" + current + ")'>" + current + "</a></li>";
                            }
                        }
                        lis += next;
                        $("#fenye").html(lis);

                    } else {
                        alert(data.msg);
                    }

                },
                fail: function (err, status) {
                    console.log(err);
                }
            });


        }


    })


}(window.jQuery);


// 自定义方法
var delete_task = function (obj) {
    if (confirm("是否继续")) {
        // 删除操作
        var datas = {"ids": obj.id + ","};
        $.ajax({
            type: 'post',
            url: '/del_task/',
            data: datas,
            success: function (str) { //返回json结果
                data = JSON.parse(str); // 解析json字符串
                // 成功和未登录都进行跳转
                if (data.code == 1 || data.code == 20000) {
                    if (data.url != "") {
                        window.location.href = data.url;
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


// 修改task
var edit_task = function (obj) {
    var title = $("#title" + obj.name).text();
    var status = 1;
    if ($("#status" + obj.name).text() == "已完成") {
        status = 2;
    }

    // 设置task的值
    $("#task_content1").val(title);
    $("#task_status_update").val(status);
    $("#task_id_getter").val(obj.name);
    $("#update_task").modal("show");
};

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
                        window.location.href = data.url;
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
                        window.location.href = data.url;
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


// 渲染task_table
var tasklist1 = function (page) {


    // 下标判断，如果是pre则判断是否为第一个
    if (page == "pre") {
        var curr = parseInt($("#current_page").text());
        if (curr == 1) {
            alert("已经是第一页了");
            return 0;
        }
        page = curr - 1;
    }

    //下标判断，如果是last判断是否为最后一个
    if (page == "last") {
        var last = parseInt($("#current_page").text());
        var curr = parseInt($("#next_page").attr('name'));

        if (curr == last) {
            alert("已经是最后一页了");
            return 0;
        }
        page = last + 1;
    }

    // 直接点击图标的情况
    if (page != "pre" && page != "last") {
        page = parseInt(page);
    }


    // 获取信息
    $.ajax({
        type: 'post',
        url: '/get_tasks/',
        data: {"page": page},
        success: function (str) { //返回json结果
            data = JSON.parse(str); // 解析json字符串
            if (data.code == 1) {
                $('table > tbody').remove();
                // 渲染模板
                $.each(data.data.datas, function (n, value) {
                    //alert(data.data.datas);
                    var trs = "";
                    var tbody = "";

                    var id = value["id"];
                    var title = value["title"];
                    var createTime = value["create_time"];

                    //动态输出状态和激活/完成按钮
                    var status;
                    var done_button;
                    if (value["status"] == "1") {
                        status = "未完成";
                        done_buuton = "<button class='am-btn am-btn-default am-btn-xs am-hide-sm-only' type='button' onclick='finish_task(this)' name='" + id + "'>" +
                            "<span class='am-icon-lock'></span> 完成</button>";

                    } else {
                        status = "已完成";
                        done_buuton = "<button class='am-btn am-btn-default am-btn-xs am-hide-sm-only' type='button' onclick='active_task(this)' name='" + id + "'>" +
                            "<span class='am-icon-repeat'></span> 激活</button>";
                    }
                    trs += "<tr><td><input type='checkbox' name='checkbox' value='" + id + "'/></td><td>" + id + "</td>" +
                        "<td><a href='#' id ='title" + id + "'>" + title + "</a></td><td id='status" + id + "'>" + status + "</td>" +
                        "<td class='am-hide-sm-only'>" + createTime + "</td>" +
                        "<td><div class='am-btn-toolbar'><div class='am-btn-group am-btn-group-xs'><button class='am-btn am-btn-default am-btn-xs am-text-secondary' type='button' onclick='edit_task(this)' name ='" + id + "'><span class='am-icon-pencil-square-o' ></span> 编辑</button>" + done_buuton + "<button type='button' id='" + id + "' onclick='delete_task(this);' class='am-btn am-btn-default am-btn-xs am-text-danger am-hide-sm-only'><span class='am-icon-trash-o' ></span> 删除</button></div></div></td></tr>";

                    tbody += trs;
                    $("#task_table").append(tbody);
                });

                // 渲染翻页
                $("#total_page").html(data.data.page_info["page_total"]);
                var last_one = data.data.page_info["page_no"];
                var lis = "<li><a href='javascript:;' id='pre_page'onclick='tasklist1(\"pre\")'>«</a></li>";
                var next = "<li><a href='javascript:;' id='next_page' onclick='tasklist1(\"last\")' name='" + last_one + "'>»</a></li>";

                //遍历li
                for (var i = 0; i < last_one; i++) {
                    var current = i + 1;
                    //如果是当前页，则渲染为激活状态，否则就不是当前页
                    if (page == current) {
                        lis += "<li class='am-active'><a href='javascript:;' id='current_page' onclick='tasklist1(" + current + ")'>" + current + "</a></li>";
                    } else {
                        lis += "<li><a href='javascript:;' onclick='tasklist1(" + current + ")'>" + current + "</a></li>";
                    }
                }
                lis += next;
                $("#fenye").html(lis);

            } else {
                alert(data.msg);
            }

        },
        fail: function (err, status) {
            console.log(err);
        }
    });


};


