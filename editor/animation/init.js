requirejs(['ext_editor_io2', 'jquery_190'],
    function (extIO, $) {
        var io = new extIO({});
        io.start();
    }
);

// //Dont change it
// requirejs(['ext_editor_2', 'jquery_190', 'raphael_210'],
//     function (ext, $, TableComponent) {

//         var cur_slide = {};

//         ext.set_start_game(function (this_e) {
//         });

//         ext.set_process_in(function (this_e, data) {
//             cur_slide["in"] = data.in[0];
//         });

//         ext.set_process_out(function (this_e, data) {
//             cur_slide["out"] = data.out[0];
//         });

//         ext.set_process_ext(function (this_e, data) {
//             cur_slide.ext = data;
//             this_e.addAnimationSlide(cur_slide);
//             cur_slide = {};
//         });

//         ext.set_process_err(function (this_e, data) {
//             cur_slide['error'] = data[0];
//             this_e.addAnimationSlide(cur_slide);
//             cur_slide = {};
//         });

//         ext.set_animate_success_slide(function (this_e, options) {
//             var $h = $(this_e.setHtmlSlide('<div class="animation-success"><div></div></div>'));
//             this_e.setAnimationHeight(115);
//         });

//         ext.set_animate_slide(function (this_e, data, options) {
//             var $content = $(this_e.setHtmlSlide(ext.get_template('animation'))).find('.animation-content');
//             if (!data) {
//                 console.log("data is undefined");
//                 return false;
//             }

//             var checkioInput = data.in[0];

//             if (data.error) {
//                 $content.find('.call').html('Fail: cowsay(' + JSON.stringify(checkioInput) + ')');
//                 $content.find('.output').html(data.error.replace(/\n/g, ","));

//                 $content.find('.output').addClass('error');
//                 $content.find('.call').addClass('error');
//                 $content.find('.answer').remove();
//                 $content.find('.explanation').remove();
//                 this_e.setAnimationHeight($content.height() + 60);
//                 return false;
//             }

//             var rightResult = data.ext["answer"];
//             var userResult = data.out;
//             var result = data.ext["result"];
//             var result_addon = data.ext["result_addon"];


//             //if you need additional info from tests (if exists)
//             var explanation = data.ext["explanation"];

//             if (typeof(userResult) === 'string') {
//                 $content.find('.output pre').text(userResult);
//             }
//             else {
//                 $content.find('.output').html('&nbsp;Your result:&nbsp;' + JSON.stringify(userResult));
//                 $content.find('.output').css('white-space', 'pre-wrap');
//             }

//             if (!result) {
//                 $content.find('.call').html('Fail: cowsay(' + JSON.stringify(checkioInput) + ')' + '<pre> _____________________\n< I did not say that! >\n ---------------------\n        \\   ^__^\n         \\  (xx)\\_______\n</pre>');
//                 $content.find('.answer pre').text(rightResult);
//                 $content.find('.answer').addClass('error');
//                 $content.find('.output').addClass('error');
//                 $content.find('.call').addClass('error');
//             }
//             else {
//                 $content.find('.call').html('Pass: cowsay(' + JSON.stringify(checkioInput) + ')');
//                 $content.find('.answer').remove();
//             }

//             this_e.setAnimationHeight($content.height() + 60);

//         });

//         var colorOrange4 = "#F0801A";
//         var colorOrange3 = "#FA8F00";
//         var colorOrange2 = "#FAA600";
//         var colorOrange1 = "#FABA00";

//         var colorBlue4 = "#294270";
//         var colorBlue3 = "#006CA9";
//         var colorBlue2 = "#65A1CF";
//         var colorBlue1 = "#8FC7ED";

//         var colorGrey4 = "#737370";
//         var colorGrey3 = "#9D9E9E";
//         var colorGrey2 = "#C5C6C6";
//         var colorGrey1 = "#EBEDED";

//         var colorWhite = "#FFFFFF";
//         //Your Additional functions or objects inside scope
//         //
//         //
//         //


//     }
// );
