<link rel="stylesheet" type="text/css" href="customcss/css/bootstrap-colorpicker.min.css" />

<script type="text/javascript">
  $LAB.script("customcss/js/bootstrap-colorpicker.min.js").wait(function() {

    var fields = {
        "primary-color": $('.navbar-primary .navbar-nav > li > a').css('color'),
        "primary-background-color": $('#topmenu .topmenu_nav .topmenu_nav_container').css('background-color'),
        "fieldset-background": $('fieldset').css('background-color'),
        "border": $('.message-list-nav-infos').css('border-bottom-color'),
        "chart-background": $('.renderer-elem').css('background-color'),
        "link": $('a').css('color'),
        "active-text": $('body').css('color'),
        "active-background": $('body').css('background-color'),
        "table-header": $('thead').css('background-color'),
        "table-row-even": $('.table-striped > tbody > tr:nth-of-type(1)').css('background-color'),
        "table-row-odd": $('.table-striped > tbody > tr:nth-of-type(2)').css('background-color'),
        "table-background": $('table').css('background-color'),
        "tooltip-text": $('.tooltip-inner').css('color'),
        "tooltip-background": $('.tooltip-inner').css('background-color'),
    };

    for ( var key in fields ) {
        $("input[name=" + key + "]").parent().colorpicker({
            color: fields[key],
            format: "hex"
        });
    }

    prewikka_resource_register({
        destroy: function() {
            $(".colorpicker-component").colorpicker("destroy");
        },
        container: "#main"
    });

  });
</script>

<div class="container">

<div class="panel panel-theme">
  <div class="panel-heading">
    <h3 class="panel-title">Actions</h3>
  </div>

  <div class="panel-body">
    <form method="post">
      <div class="form-horizontal">
        <div class="form-group">
          <label class="control-label col-sm-3">Theme:</label>
          <div class="col-sm-3">
            <select class="form-control" name="theme">
            % for theme in themes:
              <option value="${theme}" ${selected(theme == current_theme)}>${theme}</option>
            % endfor
            </select>
          </div>
          <div class="col-sm-3">
            <button type="submit" class="btn btn-default" formAction="${url_for('customcss.switch')}"><i class="fa fa-folder-open-o"></i> Load</button>
            <button type="submit" class="btn btn-danger" formAction="${url_for('customcss.remove')}"><i class="fa fa-trash"></i> Delete</button>
          </div>
        </div>
      </div>
    </form>
  </div>
</div>

<div class="panel panel-theme">
  <div class="panel-heading">
    <h3 class="panel-title">Theme ${ current_theme }</h3>
  </div>

  <div class="panel-body">
    <form method="post" action="${ url_for('customcss.save') }">
      % for category, variables in less_variables:
      <h4>${ category }</h4>
      <div class="form-horizontal">
        % for name, label in variables:
        <div class="form-group">
          <label class="control-label col-sm-5">${ label }:</label>
          <div class="input-group colorpicker-component col-sm-4">
            <input class="form-control" name="${ name }" required />
            <span class="input-group-addon"><i></i></span>
          </div>
        </div>
        % endfor
      </div>
      % endfor

      <div class="input-group col-sm-4 pull-right">
        <input class="form-control" name="theme" value="${current_theme}" required />
        <span class="input-group-btn">
          <button type="submit" class="btn btn-primary"><i class="fa fa-save"></i> Save</button>
        </span>
      </div>

    </form>
  </div>
</div>


<div style="display: none;">
  <fieldset></fieldset>
  <div class="renderer-elem"></div>
  <div class="tooltip-inner"></div>
  <div class="message-list-nav-infos"></div>
  <table class="table-striped">
    <thead></thead>
    <tbody>
      <tr class="table_row_even"></tr>
      <tr class="table_row_odd"></tr>
    </tbody>
  </table>
</div>
