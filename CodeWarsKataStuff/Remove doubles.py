
"""
import re

def doubles(s):
    s = re.sub(r"(.)\1", "", s)
    return re.sub(r"(.)\1", "", s)

"""


import re

def doubles(s):
  while re.search(r'(.)\1', s):
    s = re.sub(r'(.)\1', '', s)
  return s

"""
Test.it("Basic tests")
Test.assert_equals(doubles('abbbzz'),'ab')
Test.assert_equals(doubles('zzzzykkkd'),'ykd')
Test.assert_equals(doubles('abbcccdddda'),'aca')
Test.assert_equals(doubles('vvvvvoiiiiin'),'voin')
Test.assert_equals(doubles('rrrmooomqqqqj'),'rmomj')
Test.assert_equals(doubles('xxbnnnnnyaaaaam'),'bnyam')


'apyppoimhojfydltcdonksdhshapbetvfasexytnujnldtcgurboaefqpzlvgehjvecudbrysxyuacwnlmtffvbcjdnnyonknxubukoiukanxusaoxkznieqfbfbtdhdpbypxsqctwyakgafzczxqobowyzpfurfkzupodzoxramctesilszmwfugjkxspdkdnwfkvkpembxkxbziyinehtccexuxlbuazbugvwxhdorzyjforaxclxmkomxhaztfudfazvmtqtjlmcjyiprfsisptubqjqatrakjmvwjgfqekbkvxugswevyklkxqjpcajhzxhvokfizvlsfytypzhcqxicoieoqsnqsvqvajbwcptyvdlywuotpkycnamrntvlifletavpogdpjcgbvzgkcyyabstpajgvchavpuavflcznioqzpnshxthclbgrlphbkpffrhpwhduxrnomfmejuopmjhndqqmocgnkyotycntjesihxashbwhzianeqwdlxutheynkcgfdrvpctkudyxbtwvaeqtjlfvfkjlmytwozngujetmygfjxdvsvkyjpzcmcfhfozyesvywkdaqmhbterjzycyvkuoxxfcpablyspvfrqsmfvrmwiapxvimdvymgtcqprakoxaqmytouwtrubyusnvkodiegefsaukmkxirysohqlpsmjtzlgerjiysqcgzcbezbtmczadanibusmltqapjaicvguzbbsqbihvormkgjsqdxradwdqztbaqnikttjxldwcpzmaqukhrmvpmgecpboiboaunsaeuhtugtknyjtctmszvjvbzchcxiyxbxndzgehgatxcyicldcfyihiadlrmcljixzvodeiqlqvpizapxnhwbkyikefizrzfxhlcpcupqmdxhwywpenbsprancdowzcpjufkxnoghspkzvfisgocnlllednijzqjibqszgfzunbdxuwdxquvphngukqahvatoduwlrpxrtjoigpkaptvajgvuquzmfnfgsdjowvepvnotnfuxuwjmevefnjxileuumcgxmxlowahqkfomcwdipiwxyrjcagetnojspplilkvlmbjtchopeyfwzezijehdbcuatcafxsjugungjrepipzhznwxokpahfmbdjatjfyaetdavpnpajpdwgzqhqkoeprsnpctcrjaywrtonjyarxhmyaqnqmptposcslcourcizabugvdhwzmuetfvlgsphmdpanpuxnstinvbporkuecfrnhtlcuagifnbglqcbkkuzylcmozgpomryfiexzmypsldjhcjxmstdkcsknenwivfqtyaqyzcpgatufduckxravjdyzyhrbqjxrgnpiduhsqcijciudqecxkdlvxhagpkebormwncyigrqhgcbsqvxzspalhgugaixtoehhgtmcvqgmwlhpjbaigxhcwqkbenpdpnyfpqqfxitcreduoxcdwujslbqbxncclhwqcfpmfcauoxydsqnogwtzaypnkenzgyqoiixkpuqzwaqlfzskiuxeogfyounhwozyypnkiyoqbmcnzchbmqpcbndwdadjzkptfdrybnunhzlpasfbgdykswebmquzukzwxjfukpplhygdfoejoukahtxqrgkjpyhztndicnmotxmfldinqhknfrnlwgfeakualtebzkypxrqacyktnzrjlnlqqlcuxocaihtmwpxftkijkzuuvoqzofjeqsqbxnrmroxbeujwcrsjmpvptxungtikvhxcwglzfgutujkmbcpoinxmiylfqfsymcpstskqxiwfofdzcrxnqatqkvasnwtpjhewnkwtqjcfskbszawnsoidenpwhlehejbacsezijpsrhyfdpefqjjhzhncadypgylsfcajgrgtrykqitphjinwsyfwljeavuszorpeklcefrzvhgcyxnaxsfngyqaufybpbbewqpunymzwlplywdmjrxsxdeuxrkqjmomqkmksqulpdywpmprjdgesqfocrrihauoxkfvnyrwnmturqnsigkovsrjoxzakjpyeygrlaihvlgntvetxsyazkgjrabdezviyousjuwnrlgeusjptsanufbwghrsqkyvlzpekuihyzrmyfpjiaunewanzekxwcrqufesxvokmkomrsgcyubocznwufczexeoulkcfemiulmfacdnxrwkmejbaekalsfnkzblojnuqisadmayoogxdrjlmhenzgzyitkdgixxfuitjeaehouzgsadphbsvoxorbvjlxoakvbewidlgydthzgdocihlrnodytcfzyxirbshqkrvirpgahwlipnjgrthmnqfikpkqxyoxuyeidxpelozlxchtghocxcuczcxeghzlzfjhawpewtfabqnyxyszjlflwlfcytqeqvmvblbcvnyblkysdzsropspkeatnjhzldrpisxlykibpufkrwnhbsvzewgqgkdaoepzkmycwfejkntqnbrciknkgqntsydgjnsdgbghorsulecwdtncvnbsbrgwmschquydoysystatsxylusoshjnokyfbifimulixzaqmeniskjvradsdgpbrtncvgstezdrccknrawxmtoifkmlheyoswktsbphiwgefqfscoyrforwzkaypxworoepzxdhgfopxlbtiiquswdgovbljsbfzcjkefbdawgdjhgswndxwqclxkjrmnzufyzsauyzranilfvqnbucdbciuqcspbnkftucytzglzlypsidjiakaqnufjtqxqgbdidwnrgaiuxatlduembzzatvpifhvexfhjlexojknwiltqhcnafjprspszfsevzkvfngiehovpykupnavgkdtjmyhtaeaecgmkvructmsvnetndwknedepsdytghtzeimvviyfhmscjcayhiekoavrntzupzjcthpbzwhohgbryzvkzidxdgjymwlbtviubxvsmkbengmwerlnqycggrdwrrpysotyrnfyrzwzoavyewmpzeigawaryeimcnlktefwjqyqhvozqslglbjszpehxdwkjnmzokroxpquhsjwxzcvripxazkzyciugiditytuwrgmejpceghftacgetxobfhygamnvhrtpenljmioqacsxhlxwusbvfsiomfqpbewpgyzpismaluydrmrvqwpnylgfukxqoazjphtbomrwmskrliasydhjlqrmbfmfjijzhmlusgoabfzkrivxsvgxdlvdafvpnzazvwrxobcuvtsiafgrsitijwfmcamwsrxpvalwsvjmxrkxekfsikycoavbqqsfufuvzhlddaqayexazezwhcmyexmxpbgrokobuhdnoaooqoebpvdifqxhsnutrhlhtgysintceticdbewnoiowkliajawquclaehemkyarauwrfzfpnhdosqinbgezoizwdmgmqrwxpifmcnkgjcqnicifibquzrmwhufudksyzqqumvsdskwjirjbhkkhlbwavpnuhjamqegetumkmejazcgtgvmajhsdsepgpgenwkjtyeprotxzrkeqwatnbaymecrempjyqfsdaqmdurvzsxxnlsbnbkgqovqhsmhnjsvrhzrefuofdrcvjsanlqnxlrhetyvavqzurlohqcuokdisyprpryfwfvnymxqdmtinyxazwbdqzfgmyvhpjentfmelsnkqadoerhrcyhamfzgmwgxzlcjoalkrdhgvnlpugakuodklynblrrtkxmgurtcvqcfqnulakepaoqwmltbzgmbexqcylufnjhlkarlwqbzjfnrjlpoclhpjlhzfmktdgxzucibapbewjcfwvjpnrvwwskahwbrgvmwopbekibvaeqsdpqtofffzgfvmkwohkwpaojnhenpupjgltkgimyuhoegitqvxkhbrqdzxaluxalhjhphgkwozmucfijhibstdvwmkorspbdaegjjmrqoudegpxarcapyhijkmirqcdsxfpzyebksujrvngkdoyxigeusegddjxkbvgfkuxhwuinidjggrcehxjnwnivdkpsunzzkjyjonxdbwyvukesusibmcfenhsnmbwhjyrqdoulzcbdjfkgdezupbizbzyrwekhycxpvsktcrklrddip'
'apyoimhojfydltcdonksdhshapbetvfasexytnujnldtcgurboaefqpzlvgehjvecudbrysxyuacwnlmtvbcjdyonknxubukoiukanxusaoxkznieqfbfbtdhdpbypxsqctwyakgafzczxqobowyzpfurfkzupodzoxramctesilszmwfugjkxspdkdnwfkvkpembxkxbziyinehtexuxlbuazbugvwxhdorzyjforaxclxmkomxhaztfudfazvmtqtjlmcjyiprfsisptubqjqatrakjmvwjgfqekbkvxugswevyklkxqjpcajhzxhvokfizvlsfytypzhcqxicoieoqsnqsvqvajbwcptyvdlywuotpkycnamrntvlifletavpogdpjcgbvzgkcabstpajgvchavpuavflcznioqzpnshxthclbgrlphbkprhpwhduxrnomfmejuopmjhndmocgnkyotycntjesihxashbwhzianeqwdlxutheynkcgfdrvpctkudyxbtwvaeqtjlfvfkjlmytwozngujetmygfjxdvsvkyjpzcmcfhfozyesvywkdaqmhbterjzycyvkuofcpablyspvfrqsmfvrmwiapxvimdvymgtcqprakoxaqmytouwtrubyusnvkodiegefsaukmkxirysohqlpsmjtzlgerjiysqcgzcbezbtmczadanibusmltqapjaicvguzsqbihvormkgjsqdxradwdqztbaqnikjxldwcpzmaqukhrmvpmgecpboiboaunsaeuhtugtknyjtctmszvjvbzchcxiyxbxndzgehgatxcyicldcfyihiadlrmcljixzvodeiqlqvpizapxnhwbkyikefizrzfxhlcpcupqmdxhwywpenbsprancdowzcpjufkxnoghspkzvfisgocnlednijzqjibqszgfzunbdxuwdxquvphngukqahvatoduwlrpxrtjoigpkaptvajgvuquzmfnfgsdjowvepvnotnfuxuwjmevefnjxilemcgxmxlowahqkfomcwdipiwxyrjcagetnojslilkvlmbjtchopeyfwzezijehdbcuatcafxsjugungjrepipzhznwxokpahfmbdjatjfyaetdavpnpajpdwgzqhqkoeprsnpctcrjaywrtonjyarxhmyaqnqmptposcslcourcizabugvdhwzmuetfvlgsphmdpanpuxnstinvbporkuecfrnhtlcuagifnbglqcbuzylcmozgpomryfiexzmypsldjhcjxmstdkcsknenwivfqtyaqyzcpgatufduckxravjdyzyhrbqjxrgnpiduhsqcijciudqecxkdlvxhagpkebormwncyigrqhgcbsqvxzspalhgugaixtoegtmcvqgmwlhpjbaigxhcwqkbenpdpnyfpfxitcreduoxcdwujslbqbxnlhwqcfpmfcauoxydsqnogwtzaypnkenzgyqoxkpuqzwaqlfzskiuxeogfyounhwozpnkiyoqbmcnzchbmqpcbndwdadjzkptfdrybnunhzlpasfbgdykswebmquzukzwxjfuklhygdfoejoukahtxqrgkjpyhztndicnmotxmfldinqhknfrnlwgfeakualtebzkypxrqacyktnzrjlncuxocaihtmwpxftkijkzvoqzofjeqsqbxnrmroxbeujwcrsjmpvptxungtikvhxcwglzfgutujkmbcpoinxmiylfqfsymcpstskqxiwfofdzcrxnqatqkvasnwtpjhewnkwtqjcfskbszawnsoidenpwhlehejbacsezijpsrhyfdpefqhzhncadypgylsfcajgrgtrykqitphjinwsyfwljeavuszorpeklcefrzvhgcyxnaxsfngyqaufybpewqpunymzwlplywdmjrxsxdeuxrkqjmomqkmksqulpdywpmprjdgesqfocihauoxkfvnyrwnmturqnsigkovsrjoxzakjpyeygrlaihvlgntvetxsyazkgjrabdezviyousjuwnrlgeusjptsanufbwghrsqkyvlzpekuihyzrmyfpjiaunewanzekxwcrqufesxvokmkomrsgcyubocznwufczexeoulkcfemiulmfacdnxrwkmejbaekalsfnkzblojnuqisadmaygxdrjlmhenzgzyitkdgifuitjeaehouzgsadphbsvoxorbvjlxoakvbewidlgydthzgdocihlrnodytcfzyxirbshqkrvirpgahwlipnjgrthmnqfikpkqxyoxuyeidxpelozlxchtghocxcuczcxeghzlzfjhawpewtfabqnyxyszjlflwlfcytqeqvmvblbcvnyblkysdzsropspkeatnjhzldrpisxlykibpufkrwnhbsvzewgqgkdaoepzkmycwfejkntqnbrciknkgqntsydgjnsdgbghorsulecwdtncvnbsbrgwmschquydoysystatsxylusoshjnokyfbifimulixzaqmeniskjvradsdgpbrtncvgstezdrknrawxmtoifkmlheyoswktsbphiwgefqfscoyrforwzkaypxworoepzxdhgfopxlbtquswdgovbljsbfzcjkefbdawgdjhgswndxwqclxkjrmnzufyzsauyzranilfvqnbucdbciuqcspbnkftucytzglzlypsidjiakaqnufjtqxqgbdidwnrgaiuxatlduembatvpifhvexfhjlexojknwiltqhcnafjprspszfsevzkvfngiehovpykupnavgkdtjmyhtaeaecgmkvructmsvnetndwknedepsdytghtzeimiyfhmscjcayhiekoavrntzupzjcthpbzwhohgbryzvkzidxdgjymwlbtviubxvsmkbengmwerlnqycrdwpysotyrnfyrzwzoavyewmpzeigawaryeimcnlktefwjqyqhvozqslglbjszpehxdwkjnmzokroxpquhsjwxzcvripxazkzyciugiditytuwrgmejpceghftacgetxobfhygamnvhrtpenljmioqacsxhlxwusbvfsiomfqpbewpgyzpismaluydrmrvqwpnylgfukxqoazjphtbomrwmskrliasydhjlqrmbfmfjijzhmlusgoabfzkrivxsvgxdlvdafvpnzazvwrxobcuvtsiafgrsitijwfmcamwsrxpvalwsvjmxrkxekfsikycoavbsfufuvzhlaqayexazezwhcmyexmxpbgrokobuhdnoaqoebpvdifqxhsnutrhlhtgysintceticdbewnoiowkliajawquclaehemkyarauwrfzfpnhdosqinbgezoizwdmgmqrwxpifmcnkgjcqnicifibquzrmwhufudksyzumvsdskwjirjblbwavpnuhjamqegetumkmejazcgtgvmajhsdsepgpgenwkjtyeprotxzrkeqwatnbaymecrempjyqfsdaqmdurvzsnlsbnbkgqovqhsmhnjsvrhzrefuofdrcvjsanlqnxlrhetyvavqzurlohqcuokdisyprpryfwfvnymxqdmtinyxazwbdqzfgmyvhpjentfmelsnkqadoerhrcyhamfzgmwgxzlcjoalkrdhgvnlpugakuodklynbltkxmgurtcvqcfqnulakepaoqwmltbzgmbexqcylufnjhlkarlwqbzjfnrjlpoclhpjlhzfmktdgxzucibapbewjcfwvjpnrvskahwbrgvmwopbekibvaeqsdpqtofzgfvmkwohkwpaojnhenpupjgltkgimyuhoegitqvxkhbrqdzxaluxalhjhphgkwozmucfijhibstdvwmkorspbdaegmrqoudegpxarcapyhijkmirqcdsxfpzyebksujrvngkdoyxigeusegjxkbvgfkuxhwuinidjrcehxjnwnivdkpsunkjyjonxdbwyvukesusibmcfenhsnmbwhjyrqdoulzcbdjfkgdezupbizbzyrwekhycxpvsktcrklrip'

'apyoimhojfydltcdonksdhshapbetvfasexytnujnldtcgurboaefqpzlvgehjvecudbrysxyuacwnlmtvbcjdyonknxubukoiukanxusaoxkznieqfbfbtdhdpbypxsqctwyakgafzczxqobowyzpfurfkzupodzoxramctesilszmwfugjkxspdkdnwfkvkpembxkxbziyinehtexuxlbuazbugvwxhdorzyjforaxclxmkomxhaztfudfazvmtqtjlmcjyiprfsisptubqjqatrakjmvwjgfqekbkvxugswevyklkxqjpcajhzxhvokfizvlsfytypzhcqxicoieoqsnqsvqvajbwcptyvdlywuotpkycnamrntvlifletavpogdpjcgbvzgkcabstpajgvchavpuavflcznioqzpnshxthclbgrlphbkprhpwhduxrnomfmejuopmjhndmocgnkyotycntjesihxashbwhzianeqwdlxutheynkcgfdrvpctkudyxbtwvaeqtjlfvfkjlmytwozngujetmygfjxdvsvkyjpzcmcfhfozyesvywkdaqmhbterjzycyvkuofcpablyspvfrqsmfvrmwiapxvimdvymgtcqprakoxaqmytouwtrubyusnvkodiegefsaukmkxirysohqlpsmjtzlgerjiysqcgzcbezbtmczadanibusmltqapjaicvguzsqbihvormkgjsqdxradwdqztbaqnikjxldwcpzmaqukhrmvpmgecpboiboaunsaeuhtugtknyjtctmszvjvbzchcxiyxbxndzgehgatxcyicldcfyihiadlrmcljixzvodeiqlqvpizapxnhwbkyikefizrzfxhlcpcupqmdxhwywpenbsprancdowzcpjufkxnoghspkzvfisgocnlednijzqjibqszgfzunbdxuwdxquvphngukqahvatoduwlrpxrtjoigpkaptvajgvuquzmfnfgsdjowvepvnotnfuxuwjmevefnjxilemcgxmxlowahqkfomcwdipiwxyrjcagetnojslilkvlmbjtchopeyfwzezijehdbcuatcafxsjugungjrepipzhznwxokpahfmbdjatjfyaetdavpnpajpdwgzqhqkoeprsnpctcrjaywrtonjyarxhmyaqnqmptposcslcourcizabugvdhwzmuetfvlgsphmdpanpuxnstinvbporkuecfrnhtlcuagifnbglqcbuzylcmozgpomryfiexzmypsldjhcjxmstdkcsknenwivfqtyaqyzcpgatufduckxravjdyzyhrbqjxrgnpiduhsqcijciudqecxkdlvxhagpkebormwncyigrqhgcbsqvxzspalhgugaixtoegtmcvqgmwlhpjbaigxhcwqkbenpdpnyfpfxitcreduoxcdwujslbqbxnlhwqcfpmfcauoxydsqnogwtzaypnkenzgyqoxkpuqzwaqlfzskiuxeogfyounhwozpnkiyoqbmcnzchbmqpcbndwdadjzkptfdrybnunhzlpasfbgdykswebmquzukzwxjfuklhygdfoejoukahtxqrgkjpyhztndicnmotxmfldinqhknfrnlwgfeakualtebzkypxrqacyktnzrjlncuxocaihtmwpxftkijkzvoqzofjeqsqbxnrmroxbeujwcrsjmpvptxungtikvhxcwglzfgutujkmbcpoinxmiylfqfsymcpstskqxiwfofdzcrxnqatqkvasnwtpjhewnkwtqjcfskbszawnsoidenpwhlehejbacsezijpsrhyfdpefqhzhncadypgylsfcajgrgtrykqitphjinwsyfwljeavuszorpeklcefrzvhgcyxnaxsfngyqaufybpewqpunymzwlplywdmjrxsxdeuxrkqjmomqkmksqulpdywpmprjdgesqfocihauoxkfvnyrwnmturqnsigkovsrjoxzakjpyeygrlaihvlgntvetxsyazkgjrabdezviyousjuwnrlgeusjptsanufbwghrsqkyvlzpekuihyzrmyfpjiaunewanzekxwcrqufesxvokmkomrsgcyubocznwufczexeoulkcfemiulmfacdnxrwkmejbaekalsfnkzblojnuqisadmaygxdrjlmhenzgzyitkdgifuitjeaehouzgsadphbsvoxorbvjlxoakvbewidlgydthzgdocihlrnodytcfzyxirbshqkrvirpgahwlipnjgrthmnqfikpkqxyoxuyeidxpelozlxchtghocxcuczcxeghzlzfjhawpewtfabqnyxyszjlflwlfcytqeqvmvblbcvnyblkysdzsropspkeatnjhzldrpisxlykibpufkrwnhbsvzewgqgkdaoepzkmycwfejkntqnbrciknkgqntsydgjnsdgbghorsulecwdtncvnbsbrgwmschquydoysystatsxylusoshjnokyfbifimulixzaqmeniskjvradsdgpbrtncvgstezdrknrawxmtoifkmlheyoswktsbphiwgefqfscoyrforwzkaypxworoepzxdhgfopxlbtquswdgovbljsbfzcjkefbdawgdjhgswndxwqclxkjrmnzufyzsauyzranilfvqnbucdbciuqcspbnkftucytzglzlypsidjiakaqnufjtqxqgbdidwnrgaiuxatlduembatvpifhvexfhjlexojknwiltqhcnafjprspszfsevzkvfngiehovpykupnavgkdtjmyhtaeaecgmkvructmsvnetndwknedepsdytghtzeimiyfhmscjcayhiekoavrntzupzjcthpbzwhohgbryzvkzidxdgjymwlbtviubxvsmkbengmwerlnqycrdwpysotyrnfyrzwzoavyewmpzeigawaryeimcnlktefwjqyqhvozqslglbjszpehxdwkjnmzokroxpquhsjwxzcvripxazkzyciugiditytuwrgmejpceghftacgetxobfhygamnvhrtpenljmioqacsxhlxwusbvfsiomfqpbewpgyzpismaluydrmrvqwpnylgfukxqoazjphtbomrwmskrliasydhjlqrmbfmfjijzhmlusgoabfzkrivxsvgxdlvdafvpnzazvwrxobcuvtsiafgrsitijwfmcamwsrxpvalwsvjmxrkxekfsikycoavbsfufuvzhlaqayexazezwhcmyexmxpbgrokobuhdnoaqoebpvdifqxhsnutrhlhtgysintceticdbewnoiowkliajawquclaehemkyarauwrfzfpnhdosqinbgezoizwdmgmqrwxpifmcnkgjcqnicifibquzrmwhufudksyzumvsdskwjirjblbwavpnuhjamqegetumkmejazcgtgvmajhsdsepgpgenwkjtyeprotxzrkeqwatnbaymecrempjyqfsdaqmdurvzsnlsbnbkgqovqhsmhnjsvrhzrefuofdrcvjsanlqnxlrhetyvavqzurlohqcuokdisyprpryfwfvnymxqdmtinyxazwbdqzfgmyvhpjentfmelsnkqadoerhrcyhamfzgmwgxzlcjoalkrdhgvnlpugakuodklynbltkxmgurtcvqcfqnulakepaoqwmltbzgmbexqcylufnjhlkarlwqbzjfnrjlpoclhpjlhzfmktdgxzucibapbewjcfwvjpnrvskahwbrgvmwopbekibvaeqsdpqtofzgfvmkwohkwpaojnhenpupjgltkgimyuhoegitqvxkhbrqdzxaluxalhjhphgkwozmucfijhibstdvwmkorspbdaegmrqoudegpxarcapyhijkmirqcdsxfpzyebksujrvngkdoyxigeusegjxkbvgfkuxhwuinidjrcehxjnwnivdkpsunkjyjonxdbwyvukesusibmcfenhsnmbwhjyrqdoulzcbdjfkgdezupbizbzyrwekhycxpvsktcrklrip'

'apyoimhojfydltcdonksdhshapbetvfasexytnujnldtcgurboaefqpzlvgehjvecudbrysxyuacwnlmtvbcjdyonknxubukoiukanxusaoxkznieqfbfbtdhdpbypxsqctwyakgafzczxqobowyzpfurfkzupodzoxramctesilszmwfugjkxspdkdnwfkvkpembxkxbziyinehtexuxlbuazbugvwxhdorzyjforaxclxmkomxhaztfudfazvmtqtjlmcjyiprfsisptubqjqatrakjmvwjgfqekbkvxugswevyklkxqjpcajhzxhvokfizvlsfytypzhcqxicoieoqsnqsvqvajbwcptyvdlywuotpkycnamrntvlifletavpogdpjcgbvzgkcabstpajgvchavpuavflcznioqzpnshxthclbgrlphbkprhpwhduxrnomfmejuopmjhndmocgnkyotycntjesihxashbwhzianeqwdlxutheynkcgfdrvpctkudyxbtwvaeqtjlfvfkjlmytwozngujetmygfjxdvsvkyjpzcmcfhfozyesvywkdaqmhbterjzycyvkuofcpablyspvfrqsmfvrmwiapxvimdvymgtcqprakoxaqmytouwtrubyusnvkodiegefsaukmkxirysohqlpsmjtzlgerjiysqcgzcbezbtmczadanibusmltqapjaicvguzsqbihvormkgjsqdxradwdqztbaqnikjxldwcpzmaqukhrmvpmgecpboiboaunsaeuhtugtknyjtctmszvjvbzchcxiyxbxndzgehgatxcyicldcfyihiadlrmcljixzvodeiqlqvpizapxnhwbkyikefizrzfxhlcpcupqmdxhwywpenbsprancdowzcpjufkxnoghspkzvfisgocnlednijzqjibqszgfzunbdxuwdxquvphngukqahvatoduwlrpxrtjoigpkaptvajgvuquzmfnfgsdjowvepvnotnfuxuwjmevefnjxilemcgxmxlowahqkfomcwdipiwxyrjcagetnojslilkvlmbjtchopeyfwzezijehdbcuatcafxsjugungjrepipzhznwxokpahfmbdjatjfyaetdavpnpajpdwgzqhqkoeprsnpctcrjaywrtonjyarxhmyaqnqmptposcslcourcizabugvdhwzmuetfvlgsphmdpanpuxnstinvbporkuecfrnhtlcuagifnbglqcbuzylcmozgpomryfiexzmypsldjhcjxmstdkcsknenwivfqtyaqyzcpgatufduckxravjdyzyhrbqjxrgnpiduhsqcijciudqecxkdlvxhagpkebormwncyigrqhgcbsqvxzspalhgugaixtoegtmcvqgmwlhpjbaigxhcwqkbenpdpnyfpfxitcreduoxcdwujslbqbxnlhwqcfpmfcauoxydsqnogwtzaypnkenzgyqoxkpuqzwaqlfzskiuxeogfyounhwozpnkiyoqbmcnzchbmqpcbndwdadjzkptfdrybnunhzlpasfbgdykswebmquzukzwxjfuklhygdfoejoukahtxqrgkjpyhztndicnmotxmfldinqhknfrnlwgfeakualtebzkypxrqacyktnzrjlnllcuxocaihtmwpxftkijkzvoqzofjeqsqbxnrmroxbeujwcrsjmpvptxungtikvhxcwglzfgutujkmbcpoinxmiylfqfsymcpstskqxiwfofdzcrxnqatqkvasnwtpjhewnkwtqjcfskbszawnsoidenpwhlehejbacsezijpsrhyfdpefqhzhncadypgylsfcajgrgtrykqitphjinwsyfwljeavuszorpeklcefrzvhgcyxnaxsfngyqaufybpewqpunymzwlplywdmjrxsxdeuxrkqjmomqkmksqulpdywpmprjdgesqfocihauoxkfvnyrwnmturqnsigkovsrjoxzakjpyeygrlaihvlgntvetxsyazkgjrabdezviyousjuwnrlgeusjptsanufbwghrsqkyvlzpekuihyzrmyfpjiaunewanzekxwcrqufesxvokmkomrsgcyubocznwufczexeoulkcfemiulmfacdnxrwkmejbaekalsfnkzblojnuqisadmaygxdrjlmhenzgzyitkdgifuitjeaehouzgsadphbsvoxorbvjlxoakvbewidlgydthzgdocihlrnodytcfzyxirbshqkrvirpgahwlipnjgrthmnqfikpkqxyoxuyeidxpelozlxchtghocxcuczcxeghzlzfjhawpewtfabqnyxyszjlflwlfcytqeqvmvblbcvnyblkysdzsropspkeatnjhzldrpisxlykibpufkrwnhbsvzewgqgkdaoepzkmycwfejkntqnbrciknkgqntsydgjnsdgbghorsulecwdtncvnbsbrgwmschquydoysystatsxylusoshjnokyfbifimulixzaqmeniskjvradsdgpbrtncvgstezdrknrawxmtoifkmlheyoswktsbphiwgefqfscoyrforwzkaypxworoepzxdhgfopxlbtquswdgovbljsbfzcjkefbdawgdjhgswndxwqclxkjrmnzufyzsauyzranilfvqnbucdbciuqcspbnkftucytzglzlypsidjiakaqnufjtqxqgbdidwnrgaiuxatlduembatvpifhvexfhjlexojknwiltqhcnafjprspszfsevzkvfngiehovpykupnavgkdtjmyhtaeaecgmkvructmsvnetndwknedepsdytghtzeimiyfhmscjcayhiekoavrntzupzjcthpbzwhohgbryzvkzidxdgjymwlbtviubxvsmkbengmwerlnqycrdwpysotyrnfyrzwzoavyewmpzeigawaryeimcnlktefwjqyqhvozqslglbjszpehxdwkjnmzokroxpquhsjwxzcvripxazkzyciugiditytuwrgmejpceghftacgetxobfhygamnvhrtpenljmioqacsxhlxwusbvfsiomfqpbewpgyzpismaluydrmrvqwpnylgfukxqoazjphtbomrwmskrliasydhjlqrmbfmfjijzhmlusgoabfzkrivxsvgxdlvdafvpnzazvwrxobcuvtsiafgrsitijwfmcamwsrxpvalwsvjmxrkxekfsikycoavbsfufuvzhlaqayexazezwhcmyexmxpbgrokobuhdnoaqoebpvdifqxhsnutrhlhtgysintceticdbewnoiowkliajawquclaehemkyarauwrfzfpnhdosqinbgezoizwdmgmqrwxpifmcnkgjcqnicifibquzrmwhufudksyzumvsdskwjirjbhhlbwavpnuhjamqegetumkmejazcgtgvmajhsdsepgpgenwkjtyeprotxzrkeqwatnbaymecrempjyqfsdaqmdurvzsnlsbnbkgqovqhsmhnjsvrhzrefuofdrcvjsanlqnxlrhetyvavqzurlohqcuokdisyprpryfwfvnymxqdmtinyxazwbdqzfgmyvhpjentfmelsnkqadoerhrcyhamfzgmwgxzlcjoalkrdhgvnlpugakuodklynbltkxmgurtcvqcfqnulakepaoqwmltbzgmbexqcylufnjhlkarlwqbzjfnrjlpoclhpjlhzfmktdgxzucibapbewjcfwvjpnrvskahwbrgvmwopbekibvaeqsdpqtofzgfvmkwohkwpaojnhenpupjgltkgimyuhoegitqvxkhbrqdzxaluxalhjhphgkwozmucfijhibstdvwmkorspbdaegmrqoudegpxarcapyhijkmirqcdsxfpzyebksujrvngkdoyxigeusegjxkbvgfkuxhwuinidjrcehxjnwnivdkpsunkjyjonxdbwyvukesusibmcfenhsnmbwhjyrqdoulzcbdjfkgdezupbizbzyrwekhycxpvsktcrklrip'


def doubles(s):
    cs = []
    for c in s:
        if cs and cs[-1] == c:
            cs.pop()
        else:
            cs.append(c)
    return ''.join(cs)



import re
def doubles(s):
    while len(re.sub(r'([a-z])\1',"",s)) != len(s):
        s = re.sub(r'([a-z])\1',"",s)
    return s


import re

def doubles(s):
    res=''.join(c.group() for c in re.finditer(r'(.)\1|.', s) if len(c.group())==1)
    return doubles(res) if res!=s else res

import re

def doubles(s):
    re_double = re.compile(r'(.)\1')
    while re_double.search(s):
        s = re_double.sub('', s)
    return s


"""