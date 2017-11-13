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

