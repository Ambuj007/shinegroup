$( document ).ready(function() {
    //$("#div_id_Item").addClass("d-none");
    //var x = document.getElementsByName("inventory").elements.length;
    var x=document.getElementsByClassName("form-group")
    function toHide() {
        for (i = 0; i < x.length; i++) {
            var idd = x[i].id;

            if ($("#" + idd).parent().attr("name") == "inventory") {
                if (idd != "div_id_Item" && idd != "div_id_brand" && idd != "div_id_typep" && idd != "div_id_specificationp" && idd != "div_id_purchase_price" && idd != "div_id_selling_price" && idd != "div_id_model") {
                    $("#" + idd).addClass("d-none");
                    //console.log(x[i].id);
                }
            }
            //console.log(x[i].id);
        }
    }
    toHide();

    $("#id_Item").change(function () {
        if ($(this).val() == "CCTV") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_CCTV").removeClass("d-none");
            $("#id_CCTV").change(function () {
                if ($(this).val() == "DVR" || $(this).val() == "SMPS") {
                    $("#div_id_specificationp").addClass("d-none");
                    $("#div_id_CAMERA").addClass("d-none");
                    $("#div_id_CAMERA_SPEC").addClass("d-none");
                    $("#div_id_DVR_SMPS").removeClass("d-none");
                }

                else if ($(this).val() == "Camera") {
                    $("#div_id_specificationp").addClass("d-none");
                    $("#div_id_DVR_SMPS").addClass("d-none");
                    $("#div_id_CAMERA").removeClass("d-none");
                    $("#div_id_CAMERA_SPEC").removeClass("d-none");
                }
                else{
                    toHide();
                    $("#div_id_typep").addClass("d-none");
                    $("#div_id_CCTV").removeClass("d-none");
                    console.log($(this).val());
                }
            });
            }

        else if ($(this).val() == "Computer Peripherals") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_COMP_PERIPHERALS").removeClass("d-none");
            $("#id_COMP_PERIPHERALS").change(function () {
                if ($(this).val() == "Keyboard" || $(this).val() == "Mouse") {
                    $("#div_id_specificationp").addClass("d-none");
                    $("#div_id_SMALL_STORAGE").addClass("d-none");
                    $("#div_id_KB_MOUSE").removeClass("d-none");
                }

                else if ($(this).val() == "RAM" || $(this).val() == "GC") {
                    $("#div_id_specificationp").addClass("d-none");
                    $("#div_id_KB_MOUSE").addClass("d-none");
                    $("#div_id_SMALL_STORAGE").removeClass("d-none");
                }
                else{
                    toHide();
                    $("#div_id_typep").addClass("d-none");
                    $("#div_id_COMP_PERIPHERALS").removeClass("d-none");
                    console.log($(this).val());
                }
            });
        }

        else if ($(this).val() == "Storage") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_specificationp").addClass("d-none");
            $("#div_id_STORAGE").removeClass("d-none");
            $("#div_id_STORAGE_SPEC").removeClass("d-none");

        }

        else if ($(this).val() == "Speakers") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_specificationp").addClass("d-none");
            $("#div_id_SPEAKER").removeClass("d-none");
            $("#div_id_SPEAKER_TYPE").removeClass("d-none");

        }

        else if ($(this).val() == "Antivirus") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_specificationp").addClass("d-none");
            $("#div_id_ANTIVIRUS").removeClass("d-none");
            $("#div_id_USER").removeClass("d-none");

        }

        else if ($(this).val() == "Printer") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_PRINTER").removeClass("d-none");

        }

        else if ($(this).val() == "Ups") {
            toHide();
            $("#div_id_typep").addClass("d-none");
            $("#div_id_UPS").removeClass("d-none");

        }

        else {
            toHide();
        }

    });
    //var xx= $("td > input").get();
    //console.log(xx.length);

    $( "label" ).each(function( index ) {
        $( this ).addClass("text-light font-weight-bold");
    });
    //var xx = document.getElementsByTagName("td > input");
    //if ($("td > input").val() == "")
      //  $("td > input").removeAttr("required")



});