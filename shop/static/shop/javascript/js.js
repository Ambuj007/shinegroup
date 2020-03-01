$( document ).ready(function() {
    //$("#div_id_Item").addClass("d-none");
    //var x = document.getElementsByName("inventory").elements.length;
    var x=document.getElementsByClassName("form-group")
    function toHide() {
        for (i = 0; i < x.length; i++) {
            var idd = x[i].id;

            if ($("#" + idd).parent().attr("name") == "inventory") {
                if (idd != "div_id_item_class" && idd != "div_id_brand" && idd != "div_id_item_type" && idd != "div_id_item_specification" && idd != "div_id_purchase_price" && idd != "div_id_selling_price" && idd != "div_id_model_no") {
                    $("#" + idd).addClass("d-none");
                    //console.log(x[i].id);
                }
            }
            //console.log(x[i].id);
        }
    }
    toHide();

    $("#id_item_class").change(function () {
       // $("form")[0].reset();
        if ($(this).val() == "CCTV") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_cctv").removeClass("d-none");
            $("#id_cctv").change(function () {
                if ($(this).val() == "DVR" || $(this).val() == "SMPS") {
                    $("#div_id_item_specification").addClass("d-none");
                    $("#div_id_camera").addClass("d-none");
                    $("#div_id_camera_spec").addClass("d-none");
                    $("#div_id_dvr_smps").removeClass("d-none");
                }

                else if ($(this).val() == "Camera") {
                    $("#div_id_item_specification").addClass("d-none");
                    $("#div_id_dvr_smps").addClass("d-none");
                    $("#div_id_camera").removeClass("d-none");
                    $("#div_id_camera_spec").removeClass("d-none");
                }
                else{
                    toHide();
                    $("#div_id_item_type").addClass("d-none");
                    $("#div_id_cctv").removeClass("d-none");
                    console.log($(this).val());
                }
            });
            }

        else if ($(this).val() == "Computer Peripherals") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_comp_peripherals").removeClass("d-none");
            $("#id_comp_peripherals").change(function () {
                if ($(this).val() == "Keyboard" || $(this).val() == "Mouse") {
                    $("#div_id_item_specification").addClass("d-none");
                    $("#div_id_small_storage").addClass("d-none");
                    $("#div_id_kb_mouse").removeClass("d-none");
                }

                else if ($(this).val() == "RAM" || $(this).val() == "GC") {
                    $("#div_id_item_specification").addClass("d-none");
                    $("#div_id_kb_mouse").addClass("d-none");
                    $("#div_id_small_storage").removeClass("d-none");
                }
                else{
                    toHide();
                    $("#div_id_item_type").addClass("d-none");
                    $("#div_id_comp_peripherals").removeClass("d-none");
                    
                }
            });
        }

        else if ($(this).val() == "Storage") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_item_specification").addClass("d-none");
            $("#div_id_storage").removeClass("d-none");
            $("#div_id_storage_spec").removeClass("d-none");

        }

        else if ($(this).val() == "Speakers") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_item_specification").addClass("d-none");
            $("#div_id_speaker").removeClass("d-none");
            $("#div_id_speaker_type").removeClass("d-none");

        }

        else if ($(this).val() == "Antivirus") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_item_specification").addClass("d-none");
            $("#div_id_antivirus").removeClass("d-none");
            $("#div_id_user").removeClass("d-none");

        }

        else if ($(this).val() == "Printer") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_printer").removeClass("d-none");

        }

        else if ($(this).val() == "Ups") {
            toHide();
            $("#div_id_item_type").addClass("d-none");
            $("#div_id_ups").removeClass("d-none");

        }

        else {
            toHide();
        }

    });
    //var xx= $("td > input").get();
    //console.log(xx.length);

    // $( "label" ).each(function( index ) {

    //     $( this ).addClass("text-dark font-weight-bold");
    // });


});