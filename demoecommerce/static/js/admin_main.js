
$(function(){
    // inspect html to check id of category select dropdown.
    $(document).on('change', "select#id_category_id", function(){
        $.getJSON("/getSubcategory/",{id: $(this).val()}, function(j){
             var options = '<option value="">---------</option>';
             for (var i = 0; i < j.length; i++) {
                 options += '<option value="' + j[i].id + '">' + j[i].display_name + '</option>';
             }
             // inspect html to check id of subcategory select dropdown.
             $("select#id_subcategory_id").html(options);
         });
     });
 });
