function fillForm(json){
    console.log("fillForm");
    $.each(json, function(key, value) {
        if($('#'+key).attr('type') == 'checkbox') {
            if(value == "on"){
                $('#'+key).prop('checked', true);
            }
        }
        else{
            $('#'+key).val(value);
        }
    });



}

function csrf() {
    $.ajaxSetup({ 
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         } 
    });
}

function switchClass(){
     $('.heading').on("click", function(){
        $('i:first-child', this).toggleClass('icon-plus-sign icon-minus-sign');
    });
}

var serializeObject = function(object) {
  var arrayData, objectData;
  arrayData = object.serializeArray();
  objectData = {};

  $.each(arrayData, function() {
      objectData[this.name] = this.value || '';
  });

  return objectData;
}

var parse_recursive = function(jsonObject)
{
	var output = "";

	var type = jsonObject.type;
	var title = jsonObject.title;
	var key = jsonObject.key;

	if (type == "group")
	{
		output += "<div class='control-headings'><div class='btn btn-default heading'>"+title+"</div><ul id='" + key+ "'>";

		_.each(jsonObject.children, function(child)
		{
			output += parse_recursive(child);
		});

		output += "</ul></div>";
	}
	else if (title && type=="boolean")
	{
		output += "<div class='checkbox'><label for='"+key+"'><input name='"+key+"' type='checkbox' id='"+key+"'/><strong>"+title+"</strong></label></div>";
	}
	else if (title && type == "string")
	{
		output += "<li ><div class='form-group'><label class='control-label' for='"+key+"'>"+title+"</label><input name='"+key+"'  class='form-control id='"+key+"' type='text' name='"+key+"'/></div></li>";
	}
	else if (type == "list")
	{
		output += " <div class='form-group'><label for='"+key+"' class='control-label'>"+title+"</label><select name='"+key+"' class='form-control' id='"+key+"'>";

		$.each(jsonObject.values, function(index)
		{
			output += "<option name='" + jsonObject.labels[index] + "', value='" + jsonObject.values[index]+"'>" + jsonObject.labels[index] + "</option>";
		});

		output += "</select></div>";

	}
	return output;
}

var createJson = function(form){

    $(form).on( "submit", function( event ) {
      event.preventDefault();
      console.log( $('input, textarea, select').serialize() );
    });
}
