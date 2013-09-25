var parse_recursive = function(jsonObject)
{
	var output = "";

	var type = jsonObject.type;
	var title = jsonObject.title;
	var key = jsonObject.key;

	//if (title) {
	//	output += "<div data-role='collapsible-set'><div data-role='collapsible' data-collapsed='false'><p id='title_"+jsonObject.key+"'>"+jsonObject.title+"</p>";  
//	}
	if (type == "group")
	{
		output += "<div data-role='collapsible-set'><div data-role='collapsible' data-collapsed='false'><p id='title_"+jsonObject.key+"'>"+jsonObject.title+"</p><ul id=\"" + jsonObject.key+ "\">";

		_.each(jsonObject.children, function(child)
		{
			output += "<li>" + parse_recursive(child) + "</li>";
		});

		output += "</ul></div></div>";
	}
	else if (title && type=="boolean")
	{
		output += " <li ><label for='"+key+"'>"+title+"</label><input type='checkbox' name='"+key+"'/></li>";
	}
	else if (title && type == "string")
	{
		output += "<li ><label for='"+key+"'>"+title+"</label><input type='text' name='"+key+"'/></li>";
	}
	else if (type == "list")
	{
		output += "<select id='"+key+"'>";

		$.each(jsonObject.values, function(index)
		{
			output += "<option name='" + jsonObject.labels[index] + "', value='" + jsonObject.values[index]+"'>" + jsonObject.labels[index] + "</option>";
		});

		output += "</select>";

	}
	return output;
}


var parse_json = function(object, parentId, currentId, depth, count){
	console.log("current id"+currentId);
	if(object.type == "group"){
		$('#'+parentId).append("<li><div data-role='collapsible-set'><div data-role='collapsible' data-collapsed='false'><ul id='scheme"+currentId+"'></ul></div></div></li>");
		if(object.title){
			$('#scheme'+currentId).append("<li class='level"+depth+"'>"+object.title+"</li>");
		}
		_.each(object.children, function(child){
			
			if(child.type=="group"){
				var nextCount = count + 1;
				var nextDepth = depth - 1;
				var nextId = nextDepth.toString() + nextCount.toString();
				parse_json(child, 'scheme'+currentId, nextId, nextDepth, nextCount);
			}

			if(child.title && child.type=="boolean"){				
				$('#scheme'+currentId).append("<li class='level"+depth+"'><label for='"+child.key+"'>"+child.title+"</label><input type='checkbox' name='"+child.key+"'/></li>");
			}
			else if(child.title && child.type=="string"){
				$('#scheme'+currentId).append("<li class='level"+depth+"'><label for='"+child.key+"'>"+child.title+"</label><input name='"+child.key+"' type='text' /></li>");
			}
			
			else if(child.title && child.type=="list"){
				$('#scheme'+currentId).append("<li class='level"+depth+"'><label for='"+child.key+"'>"+child.title+"</label><select id='"+child.key+"'></li>");
				$.each(child.labels, function(index,label){
					$("#"+child.key).append("<option value='"+child.values[index]+"'>"+label+"</option>");	
				});
			}
		});
	
	}

}

getDepth = function (obj) {
    var depth = 0;
    if (obj.children) {
        obj.children.forEach(function (d) {
            var tmpDepth = getDepth(d)
            if (tmpDepth > depth) {
                depth = tmpDepth
            }
        })
    }
    return 1 + depth
}

var traverse = function(object, depth){

	if( typeof object == "object" ) {
		_.each(object, function(k,v) {
		    traverse(v, depth+1);
		});
	    }
    	else {
		$('body').append(object+depth);
    }

}
