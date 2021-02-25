1. What is the purpose of this project?

We intend to collect a large dataset of bangla sentences that can be used for
training useful language models. We intend to make the full dataset publicly
available, as well as all the codes used for collecting the dataset. We promise
to make available the full procedure of collecting the dataset so that anyone
can replicate the process as closely as possible.

2. What do we mean by large?

This depends on what the latest standard is. [Bangla Voice
Command Recognition in end-to-end System Using Topic Modeling based Contextual
Rescoring](https://ieeexplore.ieee.org/document/9053970) reports they have
collected 10 million bangla sentences. That is 10,000,000 sentences. As an
initial figure let us set our goal to 10 times that, in other words 100,000,000
sentences.

3. How does our goal dataset size compare to what is available for english?

According to [this](https://github.com/openai/gpt-3/blob/master/dataset_statistics/languages_by_word_count.csv)
GPT-3 was trained on a dataset that had 181014683608 words. Assuming about 18
words per sentence that is approximately 10,000,000,000 sentences. That is
1/100th of GPT-3 dataset.

4. Is our goal feasible?

Let us assume we get about 20 sentences per article. That means we would have
to get about 20 sentences per webpage that we scrap. However among all the
sentences we gather this way, maybe only half are unique. That means we will
only get 10 sentences per article. Under this assumption we will have to
collect 10,000,000 articles. Suppose we have 10 reputable newspaper website
publishing about 10 articles a day for the last 5 years. That gives us about
20,000 articles which is about 1/500th of our target. What this means is that
our goal may not be very feasible. We may need to invest a significant amount
of time to find good data sources and estimate how much we may actually be able
to collect.

5. Since our goal doesn't seem feasible what can we do?

We know we can collect at least 1/10th of our goal since this has already been
done. That data was collected from 42 websites. We may need to collect from
200 websites. As a first step we have to locate these sources. These can range
from news sites to blogs to literature and even legal material. Unless we have
gathered such a list of sources and estimated for each source how many
sentences we can collect from it we should not discourage ourselves.

6. What news websites can we use for our data collection?

We should focus on high quality newspapers. If sfter we have squeezed
everything out of them and still have not met our goal, we can look at lower
quality newspaper. But we must excercise extreme caution. Also newspapers
representing different political spectrum from Bangladesh and West Bengal
should be selected.

7. What is a list of good newspaper websties?
  1. [Prothom Alo](https://www.prothomalo.com/)
  2. [Daily Star](https://www.thedailystar.net/)
  3. [Kaler Kantho](https://www.kalerkantho.com/index.php)
  4. [Jugantor](https://www.jugantor.com/)
  5. [Ittefaq](https://www.ittefaq.com.bd/)
  6. [Bangladesh Pratidin](https://www.bd-pratidin.com/)
  7. [Manabzamin](https://mzamin.com/)
  10. [Janakantha](https://www.dailyjanakantha.com/)
  11. [Inqilab](https://www.dailyinqilab.com/)
  12. [Bhorer Kagoj](https://www.bhorerkagoj.com/)
  13. [TBS News](https://tbsnews.net/bangla/)
  14. [Sangbad](http://thesangbad.net/)
  15. [Naya Diganta](https://www.dailynayadiganta.com/)
  16. [Jai Jai Din](https://www.jaijaidinbd.com/)
  17. [BD News 24](https://bangla.bdnews24.com/)
  18. [Bangla Tribune](https://www.banglatribune.com/)
  19. [DMP News](https://dmpnews.org/)
  20. [UNB News](https://unb.com.bd/bangla)
  21. [Dhaka Tribune](https://bangla.dhakatribune.com/)
  22. [BBC Bangla](https://www.bbc.com/bengali)
  23. [Bonik Barta](https://bonikbarta.net/)
  24. [Share Bazar News](http://www.sharebazarnews.com/)
  25. [DW](https://www.dw.com/bn)
  26. [VOA](https://www.voabangla.com/)
  27. [Pars Today](https://parstoday.com/bn)
  28. [Anandabazar](https://parstoday.com/bn)
  29. [Aajkaal](https://www.aajkaal.in/)
  30. [Bartaman](https://bartamanpatrika.com/)
  31. [Sangbad Pratidin](https://www.sangbadpratidin.in/)
  32. [Ebela](https://ebela.in/)
  33. [Sananda](https://www.sananda.in/home)
  34. [Desh](http://www.desh.co.in/?ref=hm-Footer)
  35. [Ei Samay](https://eisamay.indiatimes.com/)
  36. [Ganadabi](http://ganadabi.com/)
  37. [Kolkata 24x7](https://www.kolkata24x7.com/)
  38. [Puber Kolom](https://www.puberkalom.com/)
  39. [Uttarbanga Sambad](https://www.uttarbangasambad.com/)
  40. [Khabar Online](https://www.khaboronline.com/)
  41. [Ganashakti](http://ganashakti.com/bengali/)
  42. [Zee News](https://zeenews.india.com/bengali)
  43. [Jagaran Tripura](http://jagarantripura.com/)
  44. [Bangla Live](https://banglalive.com/home-desktop/)
  45. [Jugasanka](https://jugasankha.in/)
  46. [America Bangla](https://americabangla.com/)
  47. [Bangla Patrika USA](https://www.banglapatrikausa.com/)
  48. [Probasher News](http://probashernews.com/)
  49. [UKBD News](http://ukbdnews.com/)
  50. [The Probashi](https://www.theprobashi.com/)
  51. [Bengali Times](https://www.thebengalitimes.com/)
  52. [Bangla Express](https://banglaexpressonline.com/)
  53. [Probash Bangla](http://www.probashbangla.org/)
  54. [Probashi Bangla](http://probashibangla.tv/)
  55. [News18](https://bengali.news18.com/)
  56. [Deshe Bideshe](https://www.deshebideshe.com/)
  57. [Sylhet Express](http://www.sylhetexpress.com/)
  58. [Daily Campus](https://thedailycampus.com/)
  59. [Biniyog Barta](https://biniyougbarta.com/)
  60. [Share Business 24](https://www.sharebusiness24.com/)
  61. [Share Market BD](https://www.sharemarketbd.com/)
  62. [Biniog Barta](https://www.biniogbarta.com/)
  63. [Share Barta 24](https://www.sharebarta24.com/)
  64. [Arthosuchak](https://www.arthosuchak.com/)
  65. [Sharebazar News](http://www.sharebazarnews.com/)
  66. [Share News 24](https://www.sharenews24.com/)
  67. [Bonik Barta](https://bonikbarta.net/)
  68. [Pujibazar](http://pujibazar.com/)
  69. [Sharebiz](https://sharebiz.net/)
  70. [Daily Stock Bangladesh](https://www.dailystockbangladesh.com/)
  71. [Ajker Bazarr](https://www.ajkerbazzar.com/)
  72. [Orthosongbad](https://orthosongbad.com/)
  73. [Sharebarta24](https://www.sharebarta24.com/)
  74. [Channel I](https://www.channelionline.com/)
  75. [Jago News 24](https://www.jagonews24.com/)
  76. [Ekushey](https://www.ekushey-tv.com/)
  77. [NTV](https://www.ntvbd.com/)
  78. [Somoy](https://www.somoynews.tv/)
  79. [Banglavision](https://banglavision.tv/)
  80. [Independent](https://banglavision.tv/)
  81. [RTV Online](https://banglavision.tv/)
  82. [Boishakhi](http://www.boishakhionline.com/)
  83. [Mohona](http://www.mohona.tv/)
  84. [Channel 24](https://www.channel24bd.tv/)
  85. [Desh TV](https://www.desh.tv/news)
  86. [My TV](http://mytvbd.tv/)
  87. [SATV](https://www.satv.tv/)
  88. [DBC](https://dbcnews.tv/)
  89. [Jamuna TV](https://www.jamuna.tv/)
  90. [News 24](https://www.news24bd.tv/)
  91. [Dainik Bartoman](http://dailybartoman.com/)
  92. [Gonokantho](http://www.gonokantho.com/)
  93. [Natun Barta](http://www.natun-barta.com/)
  94. [Sharebiz](https://sharebiz.net/)
  95. [Khabarpatra](https://khoborpatrabd.com/)
  96. [Vorer Pata](https://www.dailyvorerpata.com/)
  97. [Dhakar Dak](https://dhakardak-bd.com/)
  98. [Bangladesh Journal](https://www.bd-journal.com/)
  99. [Dainik Jagoron](https://www.dailyjagaran.com/)
  100. [Desh Rupantor](https://www.deshrupantor.com/)
  101. [Dhaka Times](https://thedhakatimes.com/)
  102. [Barta 24](https://barta24.com/)
  103. [Daily Bangladesh](https://www.daily-bangladesh.com/)
  104. [Nagorik Kantha](http://nagorikkantha.com/)
  105. [RTNN](http://www.bdrtnn.net/bangla/)
  106. [Times World 24](http://timesworld24.com/)
  107. [Purbo Pashchim](https://www.ppbd.news/)
  108. [Ronggin](http://rongginn.com/)
  109. [Sada Kalo](http://sadakalo24.com/)
  110. [Eibela](http://eibela.com/)
  111. [Dhaka Protidin](https://www.dhakaprotidin.com/)
  112. [Dainik Shiksha](http://www.dainikshiksha.com/)
  113. [Rising BD](https://www.risingbd.com/)

8. What other sources can we use?

We expect bangla blogs to be another major source of bangla text. In addition
rabindra rachanabali, narul rachanabali etc are publicly available. Bangla
wikipedia can be a good source if we can properly filter the bad content. Then
we sometimes have legally avaialable bangla books. These are sometimes scanned
copies. In that case we need to use some ocr tool (like tesseract) to extract
the text. We can gather data from already compiled datasets (fasttext, common-
crawl). Then we can go to popular facebook profiles that post in bangla and
extract the text. Finaly we can use illegally available bangla books.

9. How much can we actually collect from these sources?

We have no good estimate as of now. Each of the sources has to be taken
individually to estimate how much text can be extracted. If we fall far short
we may have to look for even extremer sources.

10. Should not we have a list of available bangla blogs?

Yes. Here is one
  1. [Muktomona](http://mukto-mona.com)
  2. [Pachforon](http://www.panchforon.in/)
  3. [BD News 24 Blog](https://blog.bdnews24.com/)
  4. [Ebela Blog](https://ebela.in/blog)
  5. [Sachalayatn](http://www.sachalayatan.com/)
  6. [Somewhereinblog](https://www.somewhereinblog.net/)
  7. [Istition Blog](https://istishon.blog/)
  8. [Bigyan](https://bigyan.org.in/)
  9. [The Wall](https://www.thewall.in/)
  10. [BanglaBlog](http://banglablog.in/)
  11. [Jojatir Jhuli](https://jojatirjhuli.net/)
  12. [TechthoughtsBD](https://techthoughtsbd.blogspot.com/)
  13. [Bong Dhong](https://bongdhong.com/)
  14. [Coffe House er Adda](http://coffeehouseradda.in/)
  15. [Fisfas](https://fisfas.wordpress.com/)
  16. [Kathar Pithe Katha](https://katharpitheykatha.blogspot.com/)
  17. [Chotoder Bangla Kobita Golpo](https://chhotoder-bangla-kobita-golpo.blogspot.com/2016/)
  18. [Abak Prithivi](https://abakprithibi.com/)
  19. [Shafayeter Blog](https://www.shafaetsplanet.com/)
  20. [German Bangla Blog](https://germanbangla.com/)
  21. [Bangla Blogs 24](https://www.banglablogs24.com/)
  22. [Priyota](https://www.priyota.xyz/)
  23. [10 minute school](https://blog.10minuteschool.com/)
  24. [Subeen](http://subeen.com/)
  25. [Andhakar Joler Kolahol](https://sonnet91.blogspot.com/)
  26. [Arup Katha](https://etongbtong.blogspot.com/)
  27. [Aloukik Hasaner Blog](https://aloukikhasan.blogspot.com/)
  28. [Cadet College Blog](http://cadetcollegeblog.com/)
  29. [Guruchandali](https://www.guruchandali.com/)
  30. [Global Voices](https://bn.globalvoices.org/)
  31. [Sahitya Cafe](https://www.sahityacafe.com/)
  32. [Choturmatrik](http://www.choturmatrik.com/)
  33. [Nari Jibon](https://banglablog-narijibon.blogspot.com/)
  34. [Jainub Khanam](https://jainub-khanam.blogspot.com/)
  35. [Moner Janala](https://sufia-eti.blogspot.com/)
  36. [Amra Bondhu](https://www.amrabondhu.com/)
  37. [eBangla](https://ebangla.org/)
  38. [Bangla Unicode](https://banglaunicode.blogspot.com/)
  39. [Ami Bangladeshi](https://amibangladeshi.blogspot.com/)
  40. [All Plants Here](https://allplantshere.blogspot.com/)
  41. [Adnan's Den](https://adnan.quaium.com/blog/)
  42. [Agdum Bagdum](https://agdumbagdum.blogspot.com/)
  43. [Nirjola Noibedyo](https://zuairijahmou.blogspot.com/)
  44. [Kali O Kalam](https://www.kaliokalam.com/)
  45. [Hrit Kalam](https://hritkalom.blogspot.com/)
  46. [Absurd Dreams](https://absurdreams.blogspot.com/)
  47. [Chora Kobita](https://chorakobita.blogspot.com/)
  48. [Biborno Akash](http://blog.biborno-akash.com/)
  49. [Konfusias](https://konfusias.blogspot.com/)
  50. [Rat Jaga Pakhi](https://ratjagapakhi.blogspot.com/)
  51. [Projapoti](https://projapoti.blogspot.com/)
  52. [Nasir Khan](https://nasir8891.wordpress.com)
  53. [Mahmud Faisal](https://mahmudfaisal.wordpress.com/)
  54. [Nana Rokom](https://nanarokom.blogspot.com/)
  55. [Slogan Dite Giye](https://sloganditegiye.blogspot.com/)
  56. [Mokabela](https://mokabela.blogspot.com/)
  57. [Mukhforr](https://mukhforr.blogspot.com/)
  58. [Projukti](https://projukti.blogspot.com/)
  59. [Biggani.org](http://biggani.org/)
  60. [Bangla Bhasha](https://bangalabhasha.blogspot.com/)
  61. [Amar Moddhe Ami](https://bhadra.wordpress.com/)
  62. [Khola Mone](https://kholamone.blogspot.com/)
  63. [Projanmo](https://projanmo.com/)
  64. [Kowtuk](https://kowtuk.blogspot.com/)
  65. [Kherokhata](https://kherokhata.blogspot.com/)
  66. [Web Pachali](https://karubasona6.blogspot.com/)
  67. [Utsa](https://utsablog.blogspot.com/)
  68. [Udvranto](https://udvranto.blogspot.com/)
  69. [Amar Ache Jol](https://bangla-blogger.blogspot.com/)
  70. [Ali Mahmed](https://www.ali-mahmed.com/)
  71. [Champs21](https://champs21.com/)
  72. [Sajsojja](http://www.sajsojja.com/)
  73. [Femina](https://www.femina.in/bengali/)
  74. [Shajgoj](https://www.shajgoj.com/)
  75. [Voltage Lab](https://blog.voltagelab.com/)
  76. [Textile Lab](https://textilelab.blogspot.com/)
  77. [Truth Seekers](https://truthseekerbanglablog.wordpress.com/)
  78. [Roaming With Wally](https://roamingwithwally.com/)
  79. [Taslima Nasrin](https://www.taslimanasrin.com/category/bangla-blogs/)
  80. [Shobuj Bangla Blog](https://shobujbanglablog.net/)
  81. [Naya Dashak](https://nayadashak.co.in/)
  82. [Anjan Dutta Lyrics](https://anjanduttalyrics.blogspot.com/)
  83. [Adorer Nouka](www.aadorernouka.in)
  84. [Aroj Ali Matubbar](https://www.arojalimatubbar.com/)
  85. [Ishan Kon](http://ishankon.com/)
  86. [Aihik](www.aihik.in)
  87. [Golpo Kobita](https://golpokobita.com/)
  88. [Charbak](https://www.charbak.com/)
  89. [Jibananda](https://jibanananda.org/)
  90. [EBoiPotro](https://eboipotro.github.io/)
  91. [Kaurab](http://www.kaurab.com/)
  92. [Baak](https://baak-archive.blogspot.com/)
  93. [Bacbichar](http://www.bacbichar.net/)
  94. [Baroyari Kobial](http://baroyarikobiyal.yolasite.com/)
  95. [Bangla Kobita Somvar](https://sahittosomvar.wordpress.com/)
  96. [Bangla Kobita](https://www.bangla-kobita.com/)
  97. [Manusher Itihash](https://manusheritihas.com/)
  98. [Tagoreweb](https://www.tagoreweb.in/)
  99. [Raashprint](http://raashprint.com/)
  100. [Bankim Rachanabali](https://bankim-rachanabali.nltr.org/)
  101. [Sharat Rachanabali](https://sarat-rachanabali.nltr.org/)
  102. [Nazrul Rachanabali](https://nazrul-rachanabali.nltr.org/)
  103. [Mrhittika](https://mrhittika.blogspot.com/)
  104. [eBangla Library](https://www.ebanglalibrary.com/)
  105. [Bibarna Kabita](https://bibarnokabita.blogspot.com/index.html)
  106. [Moner Pata](https://madhushreesengupta.blogspot.com/)
  107. [Waheed Rummon](https://waheedrummon.blogspot.com/)
  108. [Shopnolok](https://shopnolok.blogspot.com/)
  109. [Tokiz](https://tokiz.blogspot.com/)
  110. [SSSahon](https://ssshaon.blogspot.com/)
  111. [Shuvro Prakash Pal](https://shuvro.wordpress.com/)
  112. [Mahbub Sumon](ihttps://www.mahbub-sumon.com/)
  113. [Zuthochari](https://banglaspot.blogspot.com/)
  114. [Bongobani](https://bongobani.blogspot.com/index.html)
  115. [Zapito Jibon](https://valentinelover.blogspot.com/)
  116. [Dil Ka Laddu](https://xzmlx.wordpress.com/)
  117. [Parabaas](https://www.parabaas.com/)
  118. [Najmul Albab](https://najmulalbab.blogspot.com/)
  119. [Hasan Murshed](https://hasanmurshed.blogspot.com/)
  120. [Sumon Chaudhury](https://katlaharbil.blogspot.com/)
  121. [Aggatabash](https://aaggatabash.blogspot.com/)
  122. [Alpakatha Galpakatha](https://ashimul.blogspot.com/)
  123. [Mustafiz Kathan](https://mustafizblog.blogspot.com/)
  124. [Prantojoner Kotha](https://mukulbd.blogspot.com/)
  125. [Anis Mahmud](https://anismahmud.blogspot.com/)
  126. [Rajib Ahsan](https://rajibahsan.blogspot.com/)
  127. [Eternal Optimist](https://valobasha-e-ishshor.blogspot.com/)
  128. [Life In A Grain](https://life-in-a-grain.blogspot.com/)
  129. [Adda](https://uniadda.blogspot.com/)
  130. [Husainuzzaman](https://hussainuzzaman.blogspot.com/index.html)
  131. [Brammanondo](https://brammanondo.blogspot.com/)
  132. [Sagu](https://saguponda.blogspot.com/)
  133. [Dhusor Godhuli](https://dhushorgodhuli.blogspot.com/)
  134. [Kobiyal](https://kobigaan.blogspot.com/)
  135. [Koltola](https://koltola.blogspot.com/index.html)
  136. [Eita Tomar Gaan](https://eitatomargaan.blogspot.com/index.html)
  137. [Nirikh](https://nirikh.blogspot.com/)
  138. [Je Kotha Hoyni Bola](https://pgmrabi.blogspot.com/index.html)
  139. [Shuhan Rizwan](https://shuhanrizwan.com/)
  140. [Srishti](http://www.sristi.co.in/SRISTI/)
  141. [GalpoGuccho](https://galpogucchho.blogspot.com/)
  142. [Akkas Ali](https://akkasali.wordpress.com/)
  143. [Biggan Bangla](https://www.bigganbangla.com/)
  144. [Saif the boss](https://saiftheboss.com/)
  145. [Onnodrishty](http://onnodristy.com/)
  146. [Sastha Bangla](http://www.sasthabangla.com/)
  147. [Shopnobaz](http://shopnobaz.net/)
  148. [Sorolpoth](https://sorolpath.wordpress.com/)
  149. [Return Zero](https://returnzerooo.wordpress.com/)
  150. [Hello Computer](https://hellocomputer.com.bd/blog/)
  151. [Tech Tunes](https://techtunes.com.bd/#gsc.tab=0)
  152. [Tech Master](https://techmasterblog.com/)
  153. [Shamokal Darpon](https://www.shamokaldarpon.com/)
  154. [Pachforon](http://www.panchforon.in/)
  155. [Shodalap](http://shodalap.org/)
  156. [Chinta Sutra](http://www.chintasutra.com/)
  157. [Protikotha](https://protikotha.com/)
  158. [Anydhyan](http://www.anudhyan.online/)
  159. [Irabotee](https://irabotee.com/)
  160. [Shirisher Dalpala](https://shirisherdalpala.net/)
  161. [Amar Sonar Bangla](https://amarsonarbanglaamitomaybhalobasi.blogspot.com/)
  162. [Shobder Michil](https://www.sobdermichil.com/)
  163. [Anirban Surjokanto](https://anirbansurjokanto.blogspot.com/)
  164. [Ekta Kobita Ami Tumi](https://rishi026.blogspot.com/)
  165. [Muradul Islam](https://muradulislam.me/)
  166. [Khata Kobitar](https://khata-kobitar.blogspot.com/)
  167. [Megh Bangla](https://meghbangla.com/)
  168. [Kingbodontee](https://www.kingbodonty.com/)
  169. [Uthan](http://www.uthon.com/)
  170. [Sammo Raiyan](https://sammo.bangmoy.com/)
  171. [Teerandaz](http://www.teerandaz.com/)
  172. [Bong Pen](http://www.bongpen.net/)
  173. [Muktangon](https://muktangon.blog/)
  174. [Noy Number Bus](https://noynumberbus.com/)
  175. [Anya Nishad](https://anyanishad.blogspot.com/)
  176. [Granthagata](https://www.granthagata.com/)
  177. [Muktipatra](https://sohulahmed.blogspot.com/)
  178. [Ongshumali](https://www.ongshumali.com/)
  179. [Mangrove Sahitya](https://mangrovesahitya.com/)
  180. [Porospor](https://porospor.com/)
  181. [Moreechika](https://moreechikaa.wordpress.com/)
  182. [Duniyadari](https://duniyaadaari.com/)
  183. [Titikkha](https://sadiksaklayen.blogspot.com/)
  184. [Aparjan](https://aparjan.com/)
  185. [Kobi O Kobita](http://www.kobiokobita.com/)
  186. [Dr Mohammed Amin](https://draminbd.com/)
  187. [Belayet Masum](https://www.belayatmasum.com/)
  188. [Kobita Utsav](https://kobitautsov.blogspot.com/)
  189. [Rritobak](https://rritobak.blogspot.com/)
  190. [Kalimati](https://kalimationline.blogspot.com/)
  191. [Tanmay Bir](https://tanmaybir.blogspot.com/)
  192. [Sushanta Kar](https://sushantakar40.blogspot.com/)
  193. [Meghchil](https://meghchil.com/)
  194. [Galpopath](https://www.galpopath.com/)
  195. [Punoray](https://punoray.com/)
  196. [Sonar Toree](http://www.sonartoree.com)
  197. [Moloy Ray](https://morachou.blogspot.com/)
  198. [Kripa Basu](https://kripabasu.blogspot.com/)
  199. [Moloy](https://malayrc.blogspot.com/)
  200. [Samir Roy](https://samirroychoudhury.blogspot.com/)
  201. [Kalim Badsha](https://kalimbhasha.blogspot.com/)
  202. [Anubadak](https://anubadak.wordpress.com/)
  203. [Blogom Blogom Payra](https://nijermoneblogblog.wordpress.com/)
  204. [Mihinda](https://www.mihinda.com/)
  205. [Akaalbodhon](https://www.akaalbodhon.com/)
  206. [Icchekhata](https://ichhekhata.blogspot.com/)
  207. [Jolbhumi](https://jolbhumi.blogspot.com/)
  208. [Kewaos](https://kewaos.com/)
  209. [Kobitar Khata](https://priyokobita.wordpress.com/)
  210. [Tathoi](https://tathoi.blogspot.com/)
  211. [Angik Patrika](https://angickpatrika.blogspot.com/)
  212. [Shikor Mag](https://shikorrmag.blogspot.com/)
  213. [Mohapoth](https://mohapoth.wordpress.com/)
  214. [Dwitya Adhyay](https://dwitiyaadhyay.blogspot.com/)
  215. [Asma Sultana](https://meetasultana.wordpress.com/)
  216. [Kobi Anupom](https://kobianupam.blogspot.com/)
  217. [Koli Khata](https://kolikhata.wordpress.com/)
  218. [Shreya](https://shree105.blogspot.com/)
  219. [Bhuloda](https://bhulodargolpo.blogspot.com/)
  220. [Beyond the Earthly Limits](https://beyondtheearthlylimits.blogspot.com/)
  221. [Sonali Chakrabartir Kobita](https://sonalipoem.blogspot.com/)
  222. [Arabdha](https://arabdha.blogspot.com/)
  223. [Lokfolk](https://lokfolk.blogspot.com/)
  224. [Achalsiki](https://achalsiki.com/)
  225. [Banglar Mukh](https://spbanglarmukh.blogspot.com/)
  226. [Awaj Diye Jai](https://mmmainul.com/)
  227. [Janala](https://sharmaluna.com/)
  228. [Enamul Reza](https://enamulreza.wordpress.com/)
  229. [Pratichchhabi](https://pratichchhabi.blogspot.com/)
  230. [Sangbadya](https://songbadya.blogspot.com/)
  231. [O Kolkata](https://okolkata.in/)
  232. [Hojoborolo](https://choshmaebongityadi.blogspot.com/)
  233. [Chirkut](https://chirkut2011.wordpress.com/)
  234. [Walking Distance](https://walking09.blogspot.com/)
  235. [Mukto Godyo](https://muktogodya.wordpress.com/)
  236. [Itur Blog](https://ettila.blogspot.com/)
  237. [Subha Prasad](https://subhaprasad.blogspot.com/)
  238. [Mon O Mousumi](https://mon-o-mousumi.blogspot.com/)
  239. [Mutho Vora Roddur](https://muthovoraroddur.blogspot.com/)
  240. [Mollar](https://mollarsite.wordpress.com/)
  241. [Amar Srishti](https://amarsristi.blogspot.com/)
  242. [Sahitya Anjali](https://shahittoanjoly.blogspot.com/)
  243. [Ebong Ekush](https://ebongekush.blogspot.com/)
  244. [Boir Desh](http://www.boierdesh.com/)
  245. [Kabya Kantha](https://kabbokontho.wordpress.com/)
  246. [Hawagram](https://haoagram.wordpress.com/)
  247. [Sopnobilashi](https://soponbilasi.blogspot.com/)
  248. [Protishilpo](https://protishilpo.wordpress.com/)
  249. [Charpatra](https://www.chharpatra.com/)
  250. [Golpokobita](https://golpokobita.com/)
  251. [Kothaboli](https://www.kothaboli.com/)
  252. [Mtri Bhuban](https://mtribhuban.blogspot.com/)
  253. [Arun Chakraborty](https://arun-chakraborty.blogspot.com/)
  254. [Bivagiya Granthagar](https://departmental-library.blogspot.com/)
  255. [Drik](https://drikweb.blogspot.com/)
  256. [Sabdapath](https://sabdapath.com)
  257. [Soviet Books In Bengali](https://sovietbooksinbengali.blogspot.com/)
  258. [Saptahik Blackhole](https://saptahikblackholewebzine.blogspot.com/)
  259. [Akhyan Setu](https://akhyansetu.blogspot.com/)
  260. [Amader Padakkhep](https://amaderpadakkhepporibar.blogspot.com/)
  261. [Amader Bangla Kabita](https://aamaaderbanglakabita.blogspot.com/)
  262. [Alor Prithibi](https://aloprithibiblog.blogspot.com/)
  263. [Ilsheguri](https://ilseguripatrika.blogspot.com/)
  264. [Ishaner Punjo Megh](https://ishanerpunjomegh.blogspot.com/)
  265. [Mirnal O Udvash](https://nandimrinal.wordpress.com/page/2/)
  266. [Ritwik Magazine](https://ritwikmagazine.blogspot.com/)
  267. [Ebong Odhyay](https://ebongadhyaywb3rd.blogspot.com/)
  268. [Ebong Soikotha](https://ebongsoikotha.blogspot.com/)
  269. [Kobita Koridor](https://kbitakoridor.blogspot.com/)
  270. [Kobita Dihi](https://kobitadihiblogspot.blogspot.com/)
  271. [Kather Nouka](https://kathernouko.blogspot.com/)
  272. [Khorshed Alam](https://khorsed-alam.blogspot.com/)
  273. [Khoyab](https://www.khoyab.ml/)
  274. [Dehlij](https://dehlij4.blogspot.com/)
  275. [Panthojon](https://panthajon.blogspot.com/)
  276. [Golper Paraka](https://golperparaka.blogspot.com/)
  277. [Provati Medinipur](https://patrikapravatireal.blogspot.com/)
  278. [Bombay Duck](www.bombayduckmag.com)
  279. [Bangalnama](https://bangalnama.wordpress.com/)
  280. [Bamihal](https://bamihal.blogspot.com/)
  281. [Bidyut Pal](https://bidyutpal.blogspot.com/)
  282. [Bhasha Bandhan](https://bhashabandhanpotrika.blogspot.com/)
  283. [Vokatta Magazine](https://vokattamagazine.blogspot.com/)
  284. [Sabdabaul](https://sabdabaul.blogspot.com/)
  285. [Shobdomichil](https://shobdomichil.blogspot.com/)
  286. [Shunyokal](https://shunyokaal.blogspot.com/)
  287. [Sondhebelar Boishakhi](https://sondhebelarboisakhi.blogspot.com/)
  288. [Sahitya Chetona](https://sahitya-chetona.blogspot.com/)
  289. [Souti Patrika](http://soutipatrika.com/)
  290. [Sthapatya](https://sthapatyasite.wordpress.com/)
  291. [Swabhiman](https://swabhimanngo.blogspot.com/)
  292. [Akaalbodhon](https://www.akaalbodhon.com/)
  293. [Abakaashe](http://www.abakaashe.com/)
  294. [ipatrika](http://www.ipatrika.com/)
  295. [Anandakanan](http://anandapatrika.website2.me/)
  296. [Aponpath](http://aponpath.com/)
  297. [Amader Chuti](http://www.amaderchhuti.com/)
  298. [Arek Rakam](http://www.arekrakam.com/)
  299. [Alokatha](https://sites.google.com/site/alokathapd/)
  300. [Ichamoti](https://www.ichchhamoti.in/)
  301. [Iblish](https://www.iblish.in/)
  302. [Kabitashram](https://www.kabitaashram.com/)
  303. [Kalpabishwa](https://kalpabiswa.com/)
  304. [Chinno Foundation](http://chinnofoundation.org/)
  305. [Joydhak](https://joydhakweb.com/)
  306. [Jolpopotrika](https://jolpopotrika.weebly.com/)
  306. [Jaladarchi](https://www.jaladarchi.com/)
  307. [Tarunyo](https://www.tarunyo.com/)
  308. [Thokbirim](https://thokbirim.com/)
  309. [Dakshiner Janala](https://www.dakshinerjanala.com/)
  310. [Nocturne](https://nocturnemagblog.wordpress.com/)
  311. [Nibirh](http://www.nibirh.com/)
  312. [Nirmukhosh](https://nirmukhosh.in/)
  313. [Netphoring](https://www.netphoring.com/)
  314. [Potropath](https://potropath.com/)
  315. [Parichay Patrika](https://www.parichayapatrika.com/)
  316. [Protishilpo](http://protishilpo.com/)
  317. [Boishoi](https://www.boisoi.com/)
  318. [Bangla Kabita](https://www.bangla-kobita.com/)
  319. [Bangladesh Nari Pragati Songho Blog](https://bnpsbd.blogspot.com/)
  320. [Bangladesh Nari Pragati Songho Journal](https://bnps.org/journal.html)
  321. [Bindu](https://bindu.bangmoy.com/)
  322. [Voboghure Kotha](https://voboghurekotha.com/)
  323. [Bhasha Nagar](http://www.bhashanagar.com)
  324. [Vulus Recipe](http://www.vulusrecipe.com/)
  325. [Madhyabarti](http://www.madhyabarti.com/)
  326. [Mahool](http://mohool.in/)
  327. [Manchitro](http://www.manchitro.com/)
  328. [Milansagar](http://www.milansagar.com/)
  329. [Magazine Kartuz](https://www.magazinekartuj.com/)
  330. [Magic Lamp](https://www.magiclamp.net.in/)
  331. [Bengali Recipes 4u](https://bengalirecipes4u.wordpress.com/)
  332. [Shabdakunja](https://shabdakunja.com/)
  333. [Swinho](https://www.swinho.com/)
  334. [Sukumar Roy](http://sukumarray.freehostia.com/)
  335. [Harappa](http://harappa.co.in/)
  336. [Hello Testing](https://hellotestingbanglakobita.com/)
  337. [Cartoon Pattor](https://www.cartoonpattor.in/)
  338. [Narasunda](http://narashunda.com/)
  339. [Bangla Sahitya](https://banglasahityo.webs.com/)
  340. [Baarta Today](http://ritambangla.com/)
  341. [Shoily](http://shoily.com/)
  342. [Bishorgo](http://www.bishorgo.com/)
  343. [Any Tech Tune](https://anytechtune.com/)
  344. [Peace In Islam](http://www.peaceinislam.com/)
  345. [Fahimer Blog](https://sites.google.com/site/smilitude/)
  346. [Zobayer Blog](https://zobayer2009.wordpress.com/)
  347. [Progkriya](http://www.progkriya.org/)
  348. [Hukush Pakush](https://hukush-pakush.com/)
  349. [Subeen CPP Book](http://cpbook.subeen.com/)
  350. [Chorui](https://chorui12.blogspot.com/)
  351. [Faiyaz](https://itsfaiyaz.wordpress.com/)
  352. [Programming Concept](https://sites.google.com/site/programinggconcept/home)
  353. [Mukit](https://mukitmkbs.wordpress.com/)
  354. [Anindya Sundar Paul](https://anindyaspaul.com/)
  355. [Eror](https://sites.google.com/site/erorown/algorithmist)
  356. [Faiyazer Blog](https://faiazerblog.blogspot.com/)
  357. [Sharifer Blog](https://techsharif.com/)
  358. [Shokhorer Blog](https://shikhorroy.wordpress.com/)
  359. [Shakiler Blog](https://shakilcompetitiveprogramming.blogspot.com/)
  360. [Neurogen Blog](http://www.neurogenbd.com/health-blog/)
  361. [Computer Jagat](http://comjagat.com/home/articles/archive)
  362. [B-Scan](http://b-scan.org/)
  363. [Shorob](https://shorob.com/)
  364. [Samprotik Subinoy](https://shubinoymustofi.wordpress.com/)
  365. [Muktochinta](https://muktobhabna.blogspot.com/)
  366. [Golam Nobi](https://mgnabi.wordpress.com/)
  367. [Tel Gas](https://ncbd.org/)
  368. [Writing From The Street](https://humannewspaper.wordpress.com/)
  369. [TS Rahman](https://tsrahmanbd.blogspot.com/)
  370. [Muthoy Vora Alo](https://bhagshesh.blogspot.com/)
  371. [Aloy Vubon Vora](https://bilash.me/)
  372. [Etokkhone Arindam](https://etokkhonearindam.blogspot.com/)
  373. [Sumi Khan](https://sumikhanbdj.blogspot.com/)
  374. [Jibon Theke Shikhchi](https://learningfrommylife.wordpress.com/)
  375. [Darashiko](https://darashiko.com/)
  376. [Pran Kakali](https://anupsadi.blogspot.com/)
  377. [Raehat Shuvo](https://raehatshuvo.blogspot.com/)
  378. [Bratya Raisu](https://www.bratyaraisu.com/)
  379. [Mongoldhani](https://mongoldhoni.wordpress.com/)
  380. [Likhte Bashe](https://likhtebase.blogspot.com/)
  381. [Megher Onek Rong](https://megheronekrong.blogspot.com/)
  382. [Brishti Bilasini](https://brishtibilashini.blogspot.com/)
  383. [Fitness BD](https://fitnessbd.net/)
  384. [Kanak Barman](https://kanakbarman.wordpress.com/)
  385. [Kabir Aditi](https://kabiraditi.wordpress.com/)
  386. [Mehedi Haque](https://mehedihaque.blogspot.com/)
  387. [Nirjhar](https://nirjhar.com/)
  388. [Bappy Sarkar](https://bappy-sharkar.blogspot.com/)
  389. [Philasuf](https://philasuf.wordpress.com/)
  390. [Lonely Cloud](https://lonelycloud.wordpress.com/)
  391. [Kathopokathan](https://kathopokathon.wordpress.com/)
  392. [Amlan Mostakim](https://www.amlanmostakim.com/)
  393. [Nilkhota](https://nilkhota.blogspot.com/)
  394. [Sezan Mahmud](https://sezanmahmud.blogspot.com/)
  395. [New Gaul Order](https://batayon.blogspot.com/)
  396. [Ontorjatra](https://ontorjatra.blogspot.com/)
  397. [Zikobazi](https://iazico.blogspot.com/)
  398. [Kapalicana](https://kapalicana.wordpress.com/)
  399. [Ritu Pakhi](https://ritu-pakhi.blogspot.com/)
  400. [Bellayet](https://bellayet.wordpress.com/)
  401. [Rizvi](https://itsrizvi.wordpress.com/)
  402. [Mon Poboner Nao](https://nibirrashed.wordpress.com/)
  403. [Meye](https://meye2012.blogspot.com/)
  404. [Ring The Don](https://toshazed.wordpress.com/)
  405. [Ruman](https://rumansblog.wordpress.com/)
  406. [Saif Hasnat](https://www.saifhasnat.com/)
  407. [Bassbaba](https://bassblogbaba.blogspot.com/)
  408. [Nirbaan](https://nirbaan.wordpress.com/)
  409. [Naila Bari](https://nailabari.wordpress.com/)
  410. [Moner Khorak Mitai](http://www.ppdj.co.vu/)
  411. [Bangla Song Lyrics](https://banglasonglyrics.wordpress.com/)
  412. [Jeebonanondo](https://jeebonanondo.blogspot.com/index.html)

11. What should we use to scrap data from these websites?

We want to use best tool available. The best tool seems to be Scrappy.
It is in python, has a ton of good resources. However it is not the one used
by internet archive and common crawl. Internet archive uses Heritrix. This is
written in Java. Common crawl uses Apache Nutch. It is also written in Java.
Given our general dislike of Java and good experience in Python, it seems
prudent to steer clear of these two technologies in favor of Python based
Scrappy, even though these are used by highly respected institutions.

12. Should we immediatly proceed to scrap?

It seems more important to establish a process to deal with data cleaning,
tokenization and representation. This process will be common for all the
websites. But scrapping logic will be individual. What is common to all should
be dealt with first to establish firm base on which this project can be built
up. In addition this will serve as common focus point that we can come back to,
when we deal with particular issues.

13. How do we know what the challenges are in data cleaning and tokenization?

We have to collect a small dataset. We can do this by manually copying from
websites. We should collect at least 30 documents from diverse sources. Then
we will look at each text and see what the challenges are. Also we should look
at papers and other projects to see how others have done it in the past.

14. What insights have you gathered as you manually collect the data?

  1. Since our goal is to collect a dataset of sentences we should try to
 collect only valid sentences. Thus we should we ignore headers and
 sub-headers of articles as well as other metadata for now. We should try
 to collect only well-formed paragraphs where sentences are delimited by
 `।`. Then split by `।` and extract the individual sentences. Each
 sentence would then an entry in our dataset. Probably at this stage we can
 also store a reference to the next sentence. Maybe later we can exploit
 this information.
  2. One problem with above approach is that we only consider `।` as delimiter.
  But `?` an `!` are also valid sentence end indicator. In addition we must
  preserve what sentence end punctuation is used. Any symbol/punctuation other
  than `।`, `?` and `!` must be part of a sentence.
  3. We need to establish what we mean by words. After we have a sentence we
  can simply split it based on whitespace and call each token a word. But one
  problem with this approach is that there are punctuations. We do not want
  `work` and `work,` to map to independent words. Instead `work,` must be split
  into two tokens `work` and `,`. Other examples are `January-February` and
  `(adjunct)`. In each case the punctuation has to separated out as a different
  token.
  4. Also we need to consider how to deal with numbers. Taking each digit to be
  a separate token seems like a good idea.
  5. I think we can categorize our cleaning and tokenizing procedure into two
  types. The cases we have described so far are character level. We can also
  have rules that work over words.
  6. One word level rule would be to extract out common grammatical suffixes.
  These are related to number and case.
  8. We should probably look at existing bangla tokenizer and stemmers.
