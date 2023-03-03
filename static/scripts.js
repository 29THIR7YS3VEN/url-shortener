$("#text").keyup(function() {
    if ($(this).val().match(/[ ]/g, "") != null) {
        $(this).val($(this).val().replace(/[ ]/g, "_"));
    }
});