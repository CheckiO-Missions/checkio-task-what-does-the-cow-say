edge_in_onechar = 'I'
edge_out_one_char = r'''
 ___
< I >
 ---
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

base_in_one_line =  'Checkio rulezz'
base_out_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

base_in_long_without_spaces_full_line = 'loooooooooooooooooooooooooooooooooooong'
base_out_long_without_spaces_full_line = r'''
 _________________________________________
< loooooooooooooooooooooooooooooooooooong >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


base_in_long_without_spaces_two_lines = 'looooooooooooooooooooooooooooooooooooong'
base_out_long_without_spaces_two_lines = r'''
 _________________________________________
/ looooooooooooooooooooooooooooooooooooon \
\ g                                       /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


base_in_without_spaces_three_line ='loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong'
base_out_without_spaces_three_line = r'''
 _________________________________________
/ loooooooooooooooooooooooooooooooooooooo \
| oooooooooooooooooooooooooooooooooooooon |
\ g                                       /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

base_in_without_spaces_two_line_full ='looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong'
base_out_without_spaces_two_line_full = r'''
 _________________________________________
/ loooooooooooooooooooooooooooooooooooooo \
\ ooooooooooooooooooooooooooooooooooooong /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

edge_in_space_before = ' a'
edge_out_space_before = r'''
 ____
<  a >
 ----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

edge_in_space_after = 'b '
edge_out_space_after = r'''
 ____
< b  >
 ----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

edge_in_spaces_around =' c '
edge_in_many_spaces_around ='    c     '
edge_out_spaces_around = r'''
 _____
<  c  >
 -----
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

base_in_with_spaces_two_line = 'onehundredtwentytwo and one hundredfiftyone'
base_out_with_spaces_two_line = r'''
 _____________________________
/ onehundredtwentytwo and one \
\ hundredfiftyone             /
 -----------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_two_lines_with_small_start = 'A longtextwithonlyonespacetofittwolines.'
extra_out_two_lines_with_small_start = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

base_in_many_lines = ('Lorem ipsum dolor sit amet, consectetur adipisicing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')
base_out_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_long_text = """Gur Mra bs Clguba, ol Gvz Crgref  Ornhgvshy vf orggre guna htyl. Rkcyvpvg vf orggre guna vzcyvpvg. Fvzcyr vf orggre guna pbzcyrk. Pbzcyrk vf orggre guna pbzcyvpngrq. Syng vf orggre guna arfgrq. Fcnefr vf orggre guna qrafr. Ernqnovyvgl pbhagf. Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf. Nygubhtu cenpgvpnyvgl orngf chevgl. Reebef fubhyq arire cnff fvyragyl. Hayrff rkcyvpvgyl fvyraprq. Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff. Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg. Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu. Abj vf orggre guna arire. Nygubhtu arire vf bsgra orggre guna *evtug* abj. Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn. Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn. Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
extra_out_long_text = r'''
 _________________________________________
/ Gur Mra bs Clguba, ol Gvz Crgref        \
| Ornhgvshy vf orggre guna htyl. Rkcyvpvg |
| vf orggre guna vzcyvpvg. Fvzcyr vf      |
| orggre guna pbzcyrk. Pbzcyrk vf orggre  |
| guna pbzcyvpngrq. Syng vf orggre guna   |
| arfgrq. Fcnefr vf orggre guna qrafr.    |
| Ernqnovyvgl pbhagf. Fcrpvny pnfrf       |
| nera'g fcrpvny rabhtu gb oernx gur      |
| ehyrf. Nygubhtu cenpgvpnyvgl orngf      |
| chevgl. Reebef fubhyq arire cnff        |
| fvyragyl. Hayrff rkcyvpvgyl fvyraprq.   |
| Va gur snpr bs nzovthvgl, ershfr gur    |
| grzcgngvba gb thrff. Gurer fubhyq or    |
| bar-- naq cersrenoyl bayl bar --boivbhf |
| jnl gb qb vg. Nygubhtu gung jnl znl abg |
| or boivbhf ng svefg hayrff lbh'er       |
| Qhgpu. Abj vf orggre guna arire.        |
| Nygubhtu arire vf bsgra orggre guna     |
| *evtug* abj. Vs gur vzcyrzragngvba vf   |
| uneq gb rkcynva, vg'f n onq vqrn. Vs    |
| gur vzcyrzragngvba vf rnfl gb rkcynva,  |
| vg znl or n tbbq vqrn. Anzrfcnprf ner   |
| bar ubaxvat terng vqrn -- yrg'f qb zber |
\ bs gubfr!                               /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_two_lines ='mooooooooooooooooooooooooooooooooooooooo mooo'
extra_out_two_lines = r'''
 _________________________________________
/ moooooooooooooooooooooooooooooooooooooo \
\ o mooo                                  /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_39 = 'moooooooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_39 = r'''
 _________________________________________
/ moooooooooooooooooooooooooooooooooooooo \
\ mooo                                    /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_38 = 'mooooooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_38 = r'''
 ________________________________________
/ mooooooooooooooooooooooooooooooooooooo \
\ mooo                                   /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_37 = 'moooooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_37 = r'''
 _______________________________________
/ moooooooooooooooooooooooooooooooooooo \
\ mooo                                  /
 ---------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_36 = 'mooooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_36 = r'''
 ______________________________________
/ mooooooooooooooooooooooooooooooooooo \
\ mooo                                 /
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_35 = 'moooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_35 = r'''
 _____________________________________
/ moooooooooooooooooooooooooooooooooo \
\ mooo                                /
 -------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

extra_in_wrap_34 = 'mooooooooooooooooooooooooooooooooo mooo'
extra_out_wrap_34 = r'''
 _________________________________________
< mooooooooooooooooooooooooooooooooo mooo >
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

TESTS = {
    "Basics": [
        {
            "input": [base_in_one_line],
            "answer": base_out_one_line,
        },
        {
            "input": [base_in_long_without_spaces_full_line],
            "answer": base_out_long_without_spaces_full_line,
        },
        {
            "input": [base_in_long_without_spaces_two_lines],
            "answer": base_out_long_without_spaces_two_lines,
        },
        {
            "input": [base_in_without_spaces_three_line],
            "answer": base_out_without_spaces_three_line,
        },
        {
            "input": [base_in_without_spaces_two_line_full],
            "answer": base_out_without_spaces_two_line_full,
        },
        {
            "input": [base_in_with_spaces_two_line],
            "answer": base_out_with_spaces_two_line,
        },
        {
            "input": [base_in_many_lines],
            "answer": base_out_many_lines,
        },
    ],
    "Edge": [
        {
            "input": [edge_in_space_before],
            "answer": edge_out_space_before,
        },
        {
            "input": [edge_in_space_after],
            "answer": edge_out_space_after,
        },
        {
           "input": [edge_in_spaces_around],
           "answer": edge_out_spaces_around,
        },
        {
           "input": [edge_in_many_spaces_around],
           "answer": edge_out_spaces_around,
        },
        {
            "input": [edge_in_onechar],
            "answer": edge_out_one_char,
        },
    ],
    "Extra": [
        {
            "input": [extra_in_two_lines_with_small_start],
            "answer": extra_out_two_lines_with_small_start,
        },
        {
            "input": [extra_in_long_text],
            "answer": extra_out_long_text,
        },
        {
            "input": [extra_in_two_lines],
            "answer": extra_out_two_lines,
        },
        {
            "input": [extra_in_wrap_39],
            "answer": extra_out_wrap_39,
        },
        {
            "input": [extra_in_wrap_38],
            "answer": extra_out_wrap_38,
        },
        {
            "input": [extra_in_wrap_37],
            "answer": extra_out_wrap_37,
        },
        {
            "input": [extra_in_wrap_36],
            "answer": extra_out_wrap_36,
        },
        {
            "input": [extra_in_wrap_35],
            "answer": extra_out_wrap_35,
        },
        {
            "input": [extra_in_wrap_34],
            "answer": extra_out_wrap_34,
        },
    ]
}
