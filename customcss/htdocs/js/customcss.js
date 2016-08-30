function rgb2hex(orig){
    if(orig){
    var rgb = orig.replace(/\s/g,'').match(/^rgb?\((\d+),(\d+),(\d+)/i);
    return (rgb && rgb.length === 4) ? "#" +
        ("0" + parseInt(rgb[1],10).toString(16)).slice(-2) +
        ("0" + parseInt(rgb[2],10).toString(16)).slice(-2) +
        ("0" + parseInt(rgb[3],10).toString(16)).slice(-2) : orig;}
    else {
    return 0;
    }
}

function init_picker(){

    var fields = { "primary-color" : $('.navbar-primary .navbar-nav > li > a').css('color'),
                   "primary-background-color" : $('#topmenu .topmenu_nav .topmenu_nav_container').css('background-color'),
                   "fieldset-background" : $('fieldset').css('background-color'),
                   "border" : $('.message-list-nav-infos').css('border-bottom-color'),
                   "chart-background" : $('.renderer-elem').css('background-color'),
                   "link" : $('a').css('color'),
                   "active-text" : $('body').css('color'),
                   "active-background" : $('body').css('background-color'),
                   "table-header" : $('thead').css('background-color'),
                   "table-row-even" : $('.table-striped > tbody > tr:nth-of-type(1)').css('background-color'),
                   "table-row-odd" : $('.table-striped > tbody > tr:nth-of-type(2)').css('background-color'),
                   "table-background" : $('table').css('background-color')
                 };

    var fields_rgb2hex = {};

    for (var key in fields) {
        fields_rgb2hex[key] = rgb2hex(fields[key]) ;
    };

    for (var key in fields) {
        $('#' + key + ' div').css('backgroundColor', fields_rgb2hex[key]);
        $('#' + key + 'Input').val(fields_rgb2hex[key]);
        $('#' + key).ColorPicker({ color: fields_rgb2hex[key],
                                   onShow: function (colpkr) {
                                       $(colpkr).fadeIn(500);
                                       return false;
                                   },
                                   onHide: function (colpkr) {
                                       $(colpkr).fadeOut(500);
                                       return false;
                                   },
                                   onChange: function (hsb, hex, rgb) {
                                       var f = this.data('colorpicker').fieldname;
                                       $('#' + f + ' div').css('backgroundColor', '#' + hex);
                                       $('#' + f + 'Input').val('#'+hex);
                                   },
                                   fieldname: key
                                 });
    };

    $(document).on('ajaxSend', function(){
        if($("div.colorpicker")){
            $("div.colorpicker").hide();
        }
    });

}
