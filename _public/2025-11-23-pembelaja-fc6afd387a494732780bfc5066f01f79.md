---
title: 'Pembelajaran Mesin dan Integrasi Data Multi Sensor Dalam Pemetaan Stok Karbon Mangrove\xa0: Review…'
date: 2025-11-23
tags: ['mangrove', 'machine-learning', 'remote-sensing']
---

23 November 2025 · Terbit pertama di [Medium](https://medium.com/@defaniarman/pembelajaran-mesin-dan-integrasi-data-multi-sensor-dalam-pemetaan-stok-karbon-mangrove-review-e7cd06a659de) · [Semua tulisan](../blog.md)

Oleh: Defani Arman Alfitriansyah

**Pendahuluan**

Ekosistem mangrove merupakan salah satu ekosistem pesisir paling produktif yang menyimpan stok karbon sangat besar dalam biomassa pohon, bahan organik tanah, dan sedimen sebagai karbon biru yang berkontribusi pada mitigasi perubahan iklim global (Hossain et al., 2025). Indonesia memiliki luasan mangrove mencapai 3,329,459.72 hektare pada tahun 2018 yang tersebar di Pulau Papua, Sulawesi, Kalimantan, Sumatera, dan Jawa, namun menghadapi tekanan antropogenik berkelanjutan dari ekspansi akuakultur, konversi lahan, dan pembangunan infrastruktur yang mengakibatkan degradasi ekosistem (Gunawan et al., 2025). Pemantauan spasial dan temporal stok karbon mangrove menjadi kritis untuk mendukung kebijakan perubahan iklim nasional dan pengembangan pasar karbon sukarela (Roy et al., 2024).

Metode konvensional estimasi biomassa dan stok karbon mangrove mengandalkan pengukuran lapangan intensif yang memiliki keterbatasan cakupan spasial terbatas, biaya operasional tinggi, dan kesulitan akses ke daerah terpencil (Ullah et al., 2025). Teknologi penginderaan jauh satelit telah terbukti menjadi alat berharga untuk pemantauan mangrove dalam skala besar dengan biaya operasional lebih rendah (Aransiola et al., 2026). Berbagai indeks vegetasi berbasis satelit telah dikembangkan untuk estimasi stok karbon mangrove, mencakup Normalized Difference Vegetation Index (NDVI), Enhanced Vegetation Index (EVI), Soil-Adjusted Vegetation Index (SAVI), dan Mangrove Index (MI) (Purnomo Aji et al., 2023; Chen et al., 2024). Studi sebelumnya menunjukkan bahwa indeks vegetasi memiliki kemampuan bervariasi dalam mengidentifikasi mangrove dan mengestimasi hubungan karakteristik spektral dengan variabel struktural hutan seperti biomassa (Wu et al., 2025). Namun, penggunaan indeks vegetasi tunggal atau data sensor tunggal menghasilkan akurasi estimasi terbatas, terutama menghadapi variabilitas spektral tinggi akibat perbedaan spesies mangrove, struktur hutan beragam, dan pengaruh pasang surut signifikan terhadap pantulan spektral (Winarso et al., 2023).

Strategi integrasi data multisensor menggabungkan informasi dari berbagai platform penginderaan jauh, termasuk data optik multispektral (Sentinel-2 dan Landsat 8), data radar sintetis apertur (Sentinel-1 dan ALOS PALSAR-2), dan data LiDAR spasial (ICESat-2 dan GEDI) untuk menghasilkan estimasi karbon lebih akurat dan komprehensif (Pradisty et al., 2025; Simarmata et al., 2025). Penelitian terbaru menunjukkan kombinasi data optik dan SAR meningkatkan akurasi estimasi stok karbon mangrove hingga 90 persen atau lebih dibandingkan sensor tunggal, karena data optik memberikan informasi spektral dan indeks vegetasi, sementara data SAR memberikan informasi struktur biomassa unik (Chen et al., 2024; Xie et al., 2025). Algoritma pembelajaran mesin seperti Random Forest, Gradient Tree Boosting, dan neural network ensemble menunjukkan performa superior dalam menangani hubungan non-linier kompleks antara variabel spektral/SAR dan stok karbon mangrove, memberikan estimasi robust terhadap variasi lokal dan temporal (Febrianto et al., 2025; Simarmata et al., 2025). Platform komputasi cloud seperti Google Earth Engine membuat akses dan pemrosesan data satelit lebih mudah dan efisien, memungkinkan analisis multisensor dalam skala besar ( Wu et al., 2025).

Meskipun kemajuan signifikan telah dicapai, celah penelitian substansial masih ada (Roy et al., 2024). Pertama, standarisasi metodologi untuk estimasi karbon mangrove pada tingkat spesies masih belum sepenuhnya tercapai, mengingat berbagai spesies mangrove menunjukkan karakteristik spektral dan struktural berbeda (Hidayatullah et al., 2023). Kedua, estimasi karbon bawah permukaan tanah masih kurang dikaji intensif dibandingkan biomassa di atas permukaan, padahal komponen bawah tanah dapat menyimpan karbon sama atau lebih besar (Xie et al., 2025). Ketiga, penelitian dinamika temporal stok karbon mangrove masih terbatas geografis dengan keterwakilan tidak merata (Mohan et al., 2025). Diperlukan pengembangan metodologi multisensor inovatif, algoritma pembelajaran mesin lebih canggih, dan validasi lapangan komprehensif untuk meningkatkan akurasi estimasi karbon mangrove pada skala regional dan global (Roy et al., 2024; Wu et al., 2025).

Daftar Pustaka : Chapter 1

Aji, M. P., Kamal, M., & Farda, N. M. (2023). *Mangrove species mapping through phenological analysis using random forest algorithm on Google Earth Engine*. Remote Sensing Applications: Society and Environment, 30, 100978. <https://doi.org/10.1016/j.rsase.2023.100978>

Chen, Z., Zhang, H., Zhang, M., Wu, Y., & Liu, Y. (2024). *Mangrove mapping in China using Gaussian mixture model with a novel mangrove index (SSMI) derived from optical and SAR imagery*. ISPRS Journal of Photogrammetry and Remote Sensing, 218(Part A), 466–486. <https://doi.org/10.1016/j.isprsjprs.2024.09.026>

Febrianto, S., Rahman, A., Jati, O. E., Wirasatriya, A., Muskananfola, M. R., & Latifah, N. (2025). *Machine learning for mangrove species distribution using Sentinel-2 satellite imagery in Segara Anakan, Cilacap Region, Indonesia*. Regional Studies in Marine Science, 81, 103984. <https://doi.org/10.1016/j.rsma.2024.103984>

Gunawan, T. S., Hamidah, M., Rahayu, A. K., Septiani, N. N., Pingkan, J., Hermansyah, A., … Yulianto, I. (2025). *National-scale mapping of ecosystems to improve ocean accounting for marine and coastal management in Indonesia*. One Ecosystem, 10, e155166. <https://doi.org/10.3897/oneeco.10.e155166>

Hidayatullah, M. F., Kamal, M., & Wicaksono, P. (2023). *Species-based aboveground mangrove carbon stock estimation using WorldView-2 image data*. Remote Sensing Applications: Society and Environment, 30, 100959. <https://doi.org/10.1016/j.rsase.2023.100959>

Mohan, M., Roy, A. D., Montenegro, J. F., Watt, M. S., Burt, J. A., Shapiro, A., … Doaemo, W. (2025). *Mangrove forest regeneration age map and drivers of restoration success in Gulf Cooperation Council countries from satellite imagery*. Remote Sensing Applications: Society and Environment, 36, 101345. <https://doi.org/10.1016/j.rsase.2024.101345>

Roy, A. D., Arachchige, P. S. P., Watt, M. S., Kale, A., Davies, M., Heng, J. E., … Cardil, A. (2024). *Remote sensing-based mangrove blue carbon assessment in the Asia-Pacific: A systematic review*. Science of the Total Environment, 938, 173270. <https://doi.org/10.1016/j.scitotenv.2024.173270>

Simarmata, N., Wikantika, K., Tarigan, T. A., Aldyansyah, M., Tohir, R. K., Fauzi, A. I., & Fauzia, A. R. (2025). *Comparison of random forest, gradient tree boosting, and classification and regression trees for mangrove cover change monitoring using Landsat imagery*. Egyptian Journal of Remote Sensing and Space Sciences, 28(1), 138–150. <https://doi.org/10.1016/j.ejrs.2025.02.002>

Ullah, S., Nazeer, M., Wong, M. S., & Amin, G. (2025). *Remote sensing for aboveground biomass monitoring in terrestrial ecosystems: A systematic review*. Remote Sensing Applications: Society and Environment, 39, 101635. <https://doi.org/10.1016/j.rsase.2025.101635>

Wu, Y., Lu, C., Wu, K., Gao, W., Yang, N., & Lin, J. (2025). *Advancements and trends in mangrove species mapping based on remote sensing: A comprehensive review and knowledge visualization*. Global Ecology and Conservation, 57, e03408. <https://doi.org/10.1016/j.gecco.2025.e03408>

Xie, S., Li, X., Xu, Z., Ma, Z., Zhang, Z., Zhang, S., … Yang, S. (2025). *Environmental interactions drive soil organic and inorganic carbon distributions in Southeast China’s mangrove restoration areas*. CATENA, 262, 109611. <https://doi.org/10.1016/j.catena.2025.109611>

Zakir Hossain, S. M., Shams, M. B., Alromaihi, T. A., Alfaihani, A. F., Alkowari, M. A., Razzak, S. A., & Hossain, M. M. (2025). *Mangrove forestation for CO₂ sequestration, sustainable renewable energy and high-value carbons*. Sustainable Energy Technologies and Assessments, 82, 104472. <https://doi.org/10.1016/j.seta.2025.104472>

> Pembahasan lanjutan akan dilanjutkan di part berikutnya
