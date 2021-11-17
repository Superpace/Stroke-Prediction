### İnme Tahmini Uygulaması(Stroke Prediction App)
----
Bu bakmış olduğunuz uygulamada amaç kullanıcıdan alınan bilgiler ile bir model oluşturup bu oluşturulan modelden gelen sonuçları kullanıcıya yansıtmaktır.

Öncelikle Kaggle üzerinde mevcut olan [*Stroke Prediction Dataset*](https://www.kaggle.com/fedesoriano/stroke-prediction-dataset "*Stroke Prediction Dataset*") veri seti uygulamaya dahil edildi. Ardından bazı gözlemlerde bulunarak bu veri setinde bulunan özelliklerin modellerde uygulanabilmesi için bazı düzenlemelerde(gereksiz sütunların düşürülmesi, encode işlemleri, boş(null) verilerin doldurulması, ...) bulunuldu. Ardından her veri setini dahil edip ardından gözlemleyenlerin görebileceği gibi veri setinde bir dengesizlik söz konusudur. Bu dengesizlik modellerin öğrenmesini etkileyeceğinden dolayı bu veri üzerinde veri çoğaltma ve azaltma algoritmalarını içinde barındıran *SMOTEEN* metodu kullanıldı.

Verilerin uygunluğu sağlandıktan sonra, en uygun modelin seçilmesi aşamasında belirli başlı modeller denendi . Bu modellerden bazıları ; *Karar Ağaçları* (Decision Trees), *Rassal Ormanlar* (Random Forests), *XGBoost* ve* Destek Vektör Makineleridir* (SVM) . Bunlardan en iyi performans metriklerine sahip olan **XGBoost** modeli bu uygulamada esas model olarak seçildi.

Ardından yapılan tahminlemelerin kullanıcıya sunulması için bir python mikro web çerçevesi (framework) olan *Flask* kullanıldı. İlk kez bir projede kullanmış olduğum Flask yapısı ile bir form ekranının açılmasını, bu form ekranında gerekli bilgilerin alınmasını, ardından bu formdan elde edilen veriler ile yüzde kaç ihtimalle inme hastalığına yakalanabileceği bilgisininin kullanıcıya gösterimi amaçlandı.
