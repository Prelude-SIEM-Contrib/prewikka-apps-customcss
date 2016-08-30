<link rel="stylesheet" type="text/css" href="customcss/css/colorpicker.css" />
<link rel="stylesheet" type="text/css" href="customcss/css/customcss.css" />

<script type="text/javascript">
  $LAB
  .script("customcss/js/colorpicker.js")
  .script("customcss/js/customcss.js")
  .wait(function(){
    init_picker();
  });
</script>

<div class="container">

<div id="current_theme"><p style="text-align:center; font-size:20px; font-weight:bold">Curent theme : ${ cur_theme }</p></div>

<h1>New theme</h1>
<form id ="colorform" method="post" action="${ url_for('customcss.render') }">
  % for kk in ['Main Colors', 'Link and Text Colors', 'Other colors']:
  <% vv = {'Main Colors': less_main_param, 'Link and Text Colors': less_text_color, 'Other colors': less_other}[kk] %>
  <h2>${ kk }</h2>
  <div class="form-horizontal">
  % for k, v in vv.items():
    <div class="form-group">
      <label for="${ k }Input" class="control-label col-sm-5">${ v }:</label>
      <div class="col-sm-3">
        <input class="form-control" id="${ k }Input" name="${ k }" required />
      </div>
      <div id="${ k }" class ="col-sm-4 colorselector">
         <div style="background-color: #0000ff"></div>
      </div> 
    </div>
  % endfor
  </div>
  % endfor
  
  <h2>Theme Name</h2>
  <div class="form-horizontal">
    <div class="form-group">
      <label for="theme_name" class="control-label col-sm-5">Theme Name:</label>
      <div class="col-md-3">
        <input name="theme_name" id="theme_name" class="form-control" required/>
      </div>
      <div class="col-md-4">
        <button  id="CreateTheme" type ="submit" class="btn btn-primary">Create Theme File</button>    
        <input type="hidden" name="action_serv" value="Save" />
      </div>
    </div>
  </div>
</form>

<div style="height:50px" />

<h1>Change the theme</h1>
<form id ="colorform" method="post" action="${ url_for('customcss.switch')}">
  <div class="form-horizontal">
    <div class="form-group">
      <label for="name" class="control-label col-sm-5">Select the theme:</label>
      <div class="col-md-3">
        <select id="SwitchSelect" name="name" class="form-control">
          % for theme in list_themes:
          <option value="${ theme }" ${ selected(theme == cur_theme) }>${ theme }</option>
          % endfor
        </select>
      </div>
      <div class="col-md-4">
        <button type ="submit" class="btn btn-primary">Switch to this theme</button>    
      </div>
    </div>
  </div>
</form>
  
<div style="height:50px" />

<h1>Remove a theme</h1>
<form id ="colorform" method="post" action="${ url_for('customcss.remove')}">
  <div class="form-horizontal">
    <div class="form-group">
      <label for="name" class="control-label col-sm-5">Select the theme:</label>
      <div class="col-md-3">
        <select id="RemoveSelect" name="name" class="form-control">
          <option selected disabled value="disabled">-------------</option>
          % for theme in list_themes:
          % if theme not in list_base_themes:
            <option value="${ theme }">${ theme }</option>
          % endif
          % endfor
        </select>
      </div>
      <div class="col-md-4">
        <button type ="submit" class="btn btn-primary">Remove this theme</button>    
      </div>
    </div>
  </div>
</form>

</div>

<fieldset> </fieldset>
<div class="renderer-elem"> </div>
<div class="message-list-nav-infos"> </div>
<table style="display:none;" class="table-striped">
  <thead id="TestTable" style="display:none;"></thead>
  <tbody>
    <tr class="table_row_even"> </tr>
    <tr class="table_row_odd"></tr>
    <tr></tr>
  </tbody>
</table>
