"""Translates text into english and back via the Google Translate API"""

from googletrans import Translator

def translate_poems(poem_text):
    augmented = []
    for i in poem_text:
        if i.isspace() == True:
            pass
        else:
            try:
                print(i)
                translator = Translator()
                english = translator.translate(i)
                # print(english)
                backtranslation = translator.translate(english.text, dest="de")
                augmented.append(backtranslation.text)
            except ValueError:
                pass
    return augmented


translate_poems(['    ', ' Der Mond ist aufgegangen,  Die goldnen Sternlein prangen  Am Himmel hell und klar;  Der Wald steht schwarz und schweiget,  und aus den Wiesen steiget  Der weisse Nebel wunderbar. ', ' Wie ist die Welt so stille  Und in der Daemmrung Huelle  so traulich und so hold!  Als eine stille Kammer,  Wo ihr des Tages Jammer  Verschlafen und vergessen sollt. ', ' Seht ihr den Mond dort stehen? -  Er ist nur halb zu sehen  Und ist doch rund und schoen!  So sind wohl manche Sachen,  Die wir getrost belachen,  Weil unsre Augen sie nicht sehn. ', ' Wir stolze Menschenkinder  Sind eitel arme Suender  Und wissen gar nicht viel;  Wir spinnen Luftgespinste  Und suchen viele Kuenste  Und kommen weiter von dem Ziel. ', ' Gott, lass uns dein Heil schauen,  Auf nichts Vergaenglichs trauen,  Nicht Eitelkeit uns freun!  Lass uns einfaeltig werden  Und vor dir hier auf Erden  Wie Kinder fromm und froehlich sein! ', ' Wollst endlich sonder Graemen  Aus dieser Welt uns nehmen   Durch einen sanften Tod!  Und, wenn du uns genommen, Lass uns in Himmel kommen,  Du unser Herr und unser Gott! ', ' So legt euch denn, ihr Brueder,  In Gottes Namen nieder;  Kalt ist der Abendhauch.  Verschon uns, Gott! mit Strafen,  Und lass uns ruhig schlafen!  Und unsern kranken Nachbar auch! ']
)
