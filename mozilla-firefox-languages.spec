# TODO:
#   - do something with *.rdf file, there if file conflict with other lang packages
# UPDATING:
%if 0
rm -vf *.xpi
./builder -g
V=%{version}
U=http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$V/linux-i686/
curl -s $U | sed -ne 's,.*href="\([^"]\+\)/".*,'"$U"'xpi/\1.xpi,p'
%endif

Summary:	Language packs for Firefox
Summary(pl.UTF-8):	Pakiety językowe dla Firefoksa
Name:		mozilla-firefox-languages
Version:	37.0.1
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	0e7586ffb36d7a2b106b7cb4dd91e0a2
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	b04ce63911bc8feab2fb6bb00668aec9
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	d0bffa74c157c899b87abe33d6c7c809
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/az.xpi
# Source3-md5:	ba7000fa775133dbf734223343bcefa5
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source4-md5:	1111cf370263a2dee96d52938ce93d2c
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source5-md5:	f4914a52783f5c091641c9f245cfdf51
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source6-md5:	ae299df51cb0719aba9c79f8122bdc4a
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source7-md5:	84e2772041cc8b49f7876e54d8cbc9dd
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source8-md5:	1b1988c2f1bb62144c5bdb338bb6c929
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source9-md5:	adbdc8cf9df3f83cf3b431c4c51fc574
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source10-md5:	6078480ac3f39ce8bd64433baccd8b90
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source11-md5:	e4cf1506a3d4bcd766a1df1f2f2d38a9
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source12-md5:	26dcecd9d2dbd28680d9ee01d4781ec7
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source13-md5:	916b6923ea9e5d6fe113d43c8d2288b0
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source14-md5:	8a655e0d3cf3cc1e54a42002623de1cb
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	87bd63cc9dd5af7b898dcbfe5e2de957
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	7fb185c14369f350fee9588312076ab7
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	067f52aea446ac42ba7c1ba0458c1829
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/dsb.xpi
# Source18-md5:	91a67c0f5d6c8855ea0543c7fc66e7dc
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source19-md5:	d4c1a9b2cc125c8c25b823fece19a3d7
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source20-md5:	7a66dd6fb6bf86d699e071c57fcf070a
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source21-md5:	73ec7efd654425c65fbf99e5c2ed5f3f
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source22-md5:	36c51377854b13b93ae1dcc9c0453ee7
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source23-md5:	ba7eaf4f0fc47fc55ba0c73db92c4d0d
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source24-md5:	04977820cedf6ec3b5cceefb00a349a9
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source25-md5:	f8832d8f4c6b7ab14f378a1b066e6ee8
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source26-md5:	d704eecfb09f7b71a6fceb5c4b336fa3
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source27-md5:	0cfcac2fdbf74b484b0a04b8bd2eb131
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source28-md5:	2c578a7a485c15b036fee59731218dc8
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source29-md5:	f90d31cbd32b987713a6c740ea10e942
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source30-md5:	9ae7ae89a12c7e5839bf9e1c80fe676a
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source31-md5:	e710285fd8b243557afc6cc63a541bc4
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source32-md5:	59637788e1c2f8bf9847c0148967a1fa
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source33-md5:	e5cb6ab6be1ef256dc698f2b8319691d
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source34-md5:	2810b85dbae2eb36d2996a75eeb54fd4
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source35-md5:	5d24dac81f408f1682c5485f451f33b8
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source36-md5:	df3730adb7835a61e71726725c7cc712
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source37-md5:	82a7bd027c129f73b396aff219a7cd46
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source38-md5:	bdced696b2e1d1e6a83f119eb9af3c2c
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source39-md5:	9d2a335c3a7d59e212d90e39a5ec96f1
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source40-md5:	4195d0f35078534318a5de97a3716c22
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source41-md5:	20e3fc355e07cb04b5b59e28400636b4
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hsb.xpi
# Source42-md5:	c5b2fed146db979e449df89ee0908cd4
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source43-md5:	6266422c2d69cc84033d540fe52a9192
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source44-md5:	f4c00551a5c1ee4a8c71fc12b0bc680b
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source45-md5:	46b057d26990894bfa94cdb9a20ebc82
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source46-md5:	b3f9bea2fa39fbc56e5972b281c78ca4
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source47-md5:	34002e4b7736f91b463ba753645f286c
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source48-md5:	133a54a10521d39aed2803bc18c1603b
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source49-md5:	09a1f2fdc1cbafe56e21944fb4fcb908
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source50-md5:	2ef7b6d810c9714dcd6192fdb84d0644
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source51-md5:	13a18d41075350c31583b13f07874417
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source52-md5:	0b7cd6fa7436a73a29d239a995a55b78
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source53-md5:	6d7bf009d4595e310976e03c13ba4562
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source54-md5:	b30dd18714509f43230c7988da5c8bc3
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source55-md5:	819215bee1a14d9c72c9a5fae948de92
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source56-md5:	f1996827cc45ac53a12e7757f89b7c65
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source57-md5:	a393c506876f0ef0642fc66e883c5d46
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source58-md5:	170d93c88738f1fed690d9cd3b99f9f7
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source59-md5:	c96a91446ce6c2a80008785d66343e0c
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source60-md5:	040c5a58d14ccaa1980fd67bcb9d3d8e
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source61-md5:	2c1d15ca024bcc77ff97457e6b273337
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source62-md5:	8c987131a903981427e1d9b27a432091
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source63-md5:	23bf859b5515ad8f04948d9e8e3ee431
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source64-md5:	99e6b8c619d4744c24302c6f84f7254f
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source65-md5:	4692f97b0b1b3dfc80bee1299533c1bd
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source66-md5:	26cb54f76823da9308f5222ca2d89109
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source67-md5:	f09ac6ab10119980bf461fc037321743
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source68-md5:	d78df68dadc9c26c1dba3c093e42e9a4
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source69-md5:	a194d3e110b35acc07692e528b5ef56e
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source70-md5:	c75161e8c31d0090744176e088a3de46
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source71-md5:	2595a1b0d44e3f43a0aa3a5c3170c288
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source72-md5:	039e32d2a03751bdb733d4144908b352
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source73-md5:	b87e693e184abd16b328e86372250502
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source74-md5:	e43fd5c7f3779541b33aa4525c565ec1
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source75-md5:	fef81024bbbead76bb9f80fd387e8d89
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source76-md5:	0d6612f8aabc4054c480329071a97b50
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source77-md5:	2b63058a9012b8921aab4af863ec15be
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source78-md5:	df8f34295bc1e9f8973bcc058bd0395b
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source79-md5:	4c538d560cfae51b3dcc50572e4d9b72
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source80-md5:	fee2e8f163dd46f7cd0e707664511483
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source81-md5:	924a7e577eaca0ab00067bd7b0da8c44
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source82-md5:	7d08dacf83c27c9d4b22834279692e45
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source83-md5:	c8510bfb4cbd07435aa55124ce2c93ed
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uz.xpi
# Source84-md5:	d1306fccceb6573a1f4e6bec44872ce8
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source85-md5:	1538962183649263133a84790baa2def
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source86-md5:	ef0c3b7f321f2edad619eb0bb474854f
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source87-md5:	6ca1361ae382d89a8901da91eaf52da0
Source88:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source88-md5:	f9ba03b830064cc95badb94c11bbc89f
URL:		http://www.mozilla.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		firefoxdir	%{_datadir}/mozilla-firefox

%description
Language packs for Firefox.

%description -l pl.UTF-8
Pakiety językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ach
Summary:	Acoli resources for Firefox
Summary(pl.UTF-8):	Pliki językowe aczoli dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ach
Acoli resources for Firefox.

%description -n mozilla-firefox-lang-ach -l pl.UTF-8
Pliki językowe aczoli dla Firefoksa.

%package -n mozilla-firefox-lang-af
Summary:	Afrikaans resources for Firefox
Summary(pl.UTF-8):	Afrykanerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-af
Afrikaans resources for Firefox.

%description -n mozilla-firefox-lang-af -l pl.UTF-8
Afrykanerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-an
Summary:	Aragonese resources for Firefox
Summary(pl.UTF-8):	Aragońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-an
Aragonese resources for Firefox.

%description -n mozilla-firefox-lang-an -l pl.UTF-8
Aragońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ar
Summary:	Arabic resources for Firefox
Summary(pl.UTF-8):	Arabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ar
Arabic resources for Firefox.

%description -n mozilla-firefox-lang-ar -l pl.UTF-8
Arabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-as
Summary:	Assamese resources for Firefox
Summary(pl.UTF-8):	Asamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}

%description -n mozilla-firefox-lang-as
Assamese resources for Firefox.

%description -n mozilla-firefox-lang-as -l pl.UTF-8
Asamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ast
Summary:	Asturian resources for Firefox
Summary(pl.UTF-8):	Asturyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ast
Asturian resources for Firefox.

%description -n mozilla-firefox-lang-ast -l pl.UTF-8
Asturyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-az
Summary:	Azerbaijani resources for Firefox
Summary(pl.UTF-8):	Azerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-az
Azerbaijani resources for Firefox.

%description -n mozilla-firefox-lang-az -l pl.UTF-8
Azerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-be
Summary:	Belarusian resources for Firefox
Summary(pl.UTF-8):	Białoruskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-be
Belarusian resources for Firefox.

%description -n mozilla-firefox-lang-be -l pl.UTF-8
Białoruskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bg
Summary:	Bulgarian resources for Firefox
Summary(pl.UTF-8):	Bułgarskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bg
Bulgarian resources for Firefox.

%description -n mozilla-firefox-lang-bg -l pl.UTF-8
Bułgarskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bn
Summary:	Bengali (Bangladesh) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn
Bengali (Bangladesh) resources for Firefox.

%description -n mozilla-firefox-lang-bn -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Bangladeszu).

%package -n mozilla-firefox-lang-bn_IN
Summary:	Bengali (India) resources for Firefox
Summary(pl.UTF-8):	Bengalskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bn_IN
Bengali (India) resources for Firefox.

%description -n mozilla-firefox-lang-bn_IN -l pl.UTF-8
Bengalskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-br
Summary:	Breton resources for Firefox
Summary(pl.UTF-8):	Bretońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-br
Breton resources for Firefox.

%description -n mozilla-firefox-lang-br -l pl.UTF-8
Bretońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-bs
Summary:	Bosnian resources for Firefox
Summary(pl.UTF-8):	Bośniackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-bs
Bosnian resources for Firefox.

%description -n mozilla-firefox-lang-bs -l pl.UTF-8
Bośniackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.softcatala.org/projectes/mozilla/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ca
Catalan resources for Firefox.

%description -n mozilla-firefox-lang-ca -l ca.UTF-8
Recursos catalans per Firefox.

%description -n mozilla-firefox-lang-ca -l es.UTF-8
Recursos catalanes para Firefox.

%description -n mozilla-firefox-lang-ca -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cs
Summary:	Czech resources for Firefox
Summary(pl.UTF-8):	Czeskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cs
Czech resources for Firefox.

%description -n mozilla-firefox-lang-cs -l pl.UTF-8
Czeskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-csb
Summary:	Kashubian resources for Firefox
Summary(pl.UTF-8):	Kaszubskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-csb
Kashubian resources for Firefox.

%description -n mozilla-firefox-lang-csb -l pl.UTF-8
Kaszubskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-cy
Summary:	Welsh resources for Firefox
Summary(pl.UTF-8):	Walijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-cy
Welsh resources for Firefox.

%description -n mozilla-firefox-lang-cy -l pl.UTF-8
Walijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-da
Summary:	Danish resources for Firefox
Summary(pl.UTF-8):	Duńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-da
Danish resources for Firefox.

%description -n mozilla-firefox-lang-da -l pl.UTF-8
Duńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-de
Summary:	German resources for Firefox
Summary(pl.UTF-8):	Niemieckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-de
German resources for Firefox.

%description -n mozilla-firefox-lang-de -l pl.UTF-8
Niemieckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-dsb
Summary:	Lower Sorbian resources for Firefox
Summary(pl.UTF-8):	Dolnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-dsb
Lower Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-dsb -l pl.UTF-8
Dolnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-el
Summary:	Greek resources for Firefox
Summary(pl.UTF-8):	Greckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-el
Greek resources for Firefox.

%description -n mozilla-firefox-lang-el -l pl.UTF-8
Greckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_GB
Summary:	English (British) resources for Firefox
Summary(pl.UTF-8):	Angielskie (brytyjskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_GB
English (British) resources for Firefox.

%description -n mozilla-firefox-lang-en_GB -l pl.UTF-8
Angielskie (brytyjskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_US
Summary:	English (American) resources for Firefox
Summary(pl.UTF-8):	Angielskie (amerykańskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_US
English (American) resources for Firefox.

%description -n mozilla-firefox-lang-en_US -l pl.UTF-8
Angielskie (amerykańskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-en_ZA
Summary:	English (South Africa) resources for Firefox
Summary(pl.UTF-8):	Angielskie pliki językowe dla Firefoksa (wersja dla RPA)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-en_ZA
English (South Africa) resources for Firefox.

%description -n mozilla-firefox-lang-en_ZA -l pl.UTF-8
Angielskie pliki językowe dla Firefoksa (wersja dla Republiki
Południowej Afryki).

%package -n mozilla-firefox-lang-eo
Summary:	Esperanto resources for Firefox
Summary(pl.UTF-8):	Pliki językowe esperanto dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eo
Esperanto resources for Firefox.

%description -n mozilla-firefox-lang-eo -l pl.UTF-8
Pliki językowe esperanto dla Firefoksa.

%package -n mozilla-firefox-lang-es_AR
Summary:	Spanish (Andorra) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Andorra) per Firefox
Summary(es.UTF-8):	Recursos españoles (Andorra) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_AR
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es_AR -l ca.UTF-8
Recursos espanyols (Andorra) per Firefox.

%description -n mozilla-firefox-lang-es_AR -l es.UTF-8
Recursos españoles (Andorra) para Firefox.

%description -n mozilla-firefox-lang-es_AR -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Andory).

%package -n mozilla-firefox-lang-es_CL
Summary:	Spanish (Chile) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Xile) per Firefox
Summary(es.UTF-8):	Recursos españoles (Chile) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_CL
Spanish (Chile) resources for Firefox.

%description -n mozilla-firefox-lang-es_CL -l ca.UTF-8
Recursos espanyols (Xile) per Firefox.

%description -n mozilla-firefox-lang-es_CL -l es.UTF-8
Recursos españoles (Chile) para Firefox.

%description -n mozilla-firefox-lang-es_CL -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Chile).

%package -n mozilla-firefox-lang-es
Summary:	Spanish (Spain) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Espanya) per Firefox
Summary(es.UTF-8):	Recursos españoles (España) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es
Spanish (Spain) resources for Firefox.

%description -n mozilla-firefox-lang-es -l ca.UTF-8
Recursos espanyols (Espanya) per Firefox.

%description -n mozilla-firefox-lang-es -l es.UTF-8
Recursos españoles (España) para Firefox.

%description -n mozilla-firefox-lang-es -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Hiszpanii).

%package -n mozilla-firefox-lang-es_MX
Summary:	Spanish (Mexico) resources for Firefox
Summary(ca.UTF-8):	Recursos espanyols (Mèxic) per Firefox
Summary(es.UTF-8):	Recursos españoles (México) para Firefox
Summary(pl.UTF-8):	Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-es_MX
Spanish (Mexico) resources for Firefox.

%description -n mozilla-firefox-lang-es_MX -l ca.UTF-8
Recursos espanyols (Mèxic) per Firefox.

%description -n mozilla-firefox-lang-es_MX -l es.UTF-8
Recursos españoles (México) para Firefox.

%description -n mozilla-firefox-lang-es_MX -l pl.UTF-8
Hiszpańskie pliki językowe dla Firefoksa (wersja dla Meksyku).

%package -n mozilla-firefox-lang-et
Summary:	Estonian resources for Firefox
Summary(pl.UTF-8):	Estońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-et
Estonian resources for Firefox.

%description -n mozilla-firefox-lang-et -l pl.UTF-8
Estońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-eu
Summary:	Basque resources for Firefox
Summary(pl.UTF-8):	Baskijskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-eu
Basque resources for Firefox.

%description -n mozilla-firefox-lang-eu -l pl.UTF-8
Baskijskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fa
Summary:	Persian resources for Firefox
Summary(pl.UTF-8):	Perskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fa
Persian resources for Firefox.

%description -n mozilla-firefox-lang-fa -l pl.UTF-8
Perskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ff
Summary:	Fulah resources for Firefox
Summary(pl.UTF-8):	Pliki językowe fulani dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ff
Fulah resources for Firefox.

%description -n mozilla-firefox-lang-ff -l pl.UTF-8
Pliki językowe fulani dla Firefoksa.

%package -n mozilla-firefox-lang-fi
Summary:	Finnish resources for Firefox
Summary(pl.UTF-8):	Fińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fi
Finnish resources for Firefox.

%description -n mozilla-firefox-lang-fi -l pl.UTF-8
Fińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fr
Summary:	French resources for Firefox
Summary(pl.UTF-8):	Francuskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fr
French resources for Firefox.

%description -n mozilla-firefox-lang-fr -l pl.UTF-8
Francuskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-fy
Summary:	Frisian resources for Firefox
Summary(pl.UTF-8):	Fryzyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-fy
Frisian resources for Firefox.

%description -n mozilla-firefox-lang-fy -l pl.UTF-8
Fryzyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ga
Summary:	Irish resources for Firefox
Summary(pl.UTF-8):	Irlandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ga
Irish resources for Firefox.

%description -n mozilla-firefox-lang-ga -l pl.UTF-8
Irlandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gd
Summary:	Gaelic resources for Firefox
Summary(pl.UTF-8):	Szkockie (gaelickie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gd
Gaelic resources for Firefox.

%description -n mozilla-firefox-lang-gd -l pl.UTF-8
Szkockie (gaelickie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gl
Summary:	Galician resources for Firefox
Summary(pl.UTF-8):	Galicyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gl
Galician resources for Firefox.

%description -n mozilla-firefox-lang-gl -l pl.UTF-8
Galicyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-gu
Summary:	Gujarati resources for Firefox
Summary(pl.UTF-8):	Pliki językowe gudźarati dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-gu
Gujarati resources for Firefox.

%description -n mozilla-firefox-lang-gu -l pl.UTF-8
Pliki językowe gudźarati dla Firefoksa.

%package -n mozilla-firefox-lang-he
Summary:	Hebrew resources for Firefox
Summary(pl.UTF-8):	Hebrajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-he
Hebrew resources for Firefox.

%description -n mozilla-firefox-lang-he -l pl.UTF-8
Hebrajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hi
Summary:	Hindi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe hindi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hi
Hindi resources for Firefox.

%description -n mozilla-firefox-lang-hi -l pl.UTF-8
Pliki językowe hindi dla Firefoksa.

%package -n mozilla-firefox-lang-hr
Summary:	Croatian resources for Firefox
Summary(pl.UTF-8):	Chorwackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hr
Croatian resources for Firefox.

%description -n mozilla-firefox-lang-hr -l pl.UTF-8
Chorwackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hsb
Summary:	Upper Sorbian resources for Firefox
Summary(pl.UTF-8):	Górnołużyckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hsb
Upper Sorbian resources for Firefox.

%description -n mozilla-firefox-lang-hsb -l pl.UTF-8
Górnołużyckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hu
Summary:	Hungarian resources for Firefox
Summary(hu.UTF-8):	Magyar nyelv Firefox-hez
Summary(pl.UTF-8):	Węgierskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hu
Hungarian resources for Firefox.

%description -n mozilla-firefox-lang-hu -l hu.UTF-8
Magyar nyelv Firefox-hez.

%description -n mozilla-firefox-lang-hu -l pl.UTF-8
Węgierskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-hy
Summary:	Armenian resources for Firefox
Summary(pl.UTF-8):	Ormiańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-hy
Armenian resources for Firefox.

%description -n mozilla-firefox-lang-hy -l pl.UTF-8
Ormiańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-id
Summary:	Indonesian resources for Firefox
Summary(pl.UTF-8):	Indonezyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-id
Indonesian resources for Firefox.

%description -n mozilla-firefox-lang-id -l pl.UTF-8
Indonezyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-is
Summary:	Icelandic resources for Firefox
Summary(pl.UTF-8):	Islandzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-is
Icelandic resources for Firefox.

%description -n mozilla-firefox-lang-is -l pl.UTF-8
Islandzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-it
Summary:	Italian resources for Firefox
Summary(pl.UTF-8):	Włoskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-it
Italian resources for Firefox.

%description -n mozilla-firefox-lang-it -l pl.UTF-8
Włoskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ja
Summary:	Japanese resources for Firefox
Summary(pl.UTF-8):	Japońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ja
Japanese resources for Firefox.

%description -n mozilla-firefox-lang-ja -l pl.UTF-8
Japońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kk
Summary:	Kazakh resources for Firefox
Summary(pl.UTF-8):	Kazachskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kk
Kazakh resources for Firefox.

%description -n mozilla-firefox-lang-kk -l pl.UTF-8
Kazachskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-km
Summary:	Khmer resources for Firefox
Summary(pl.UTF-8):	Khmerskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-km
Khmer resources for Firefox.

%description -n mozilla-firefox-lang-km -l pl.UTF-8
Khmerskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-kn
Summary:	Kannada resources for Firefox
Summary(pl.UTF-8):	Pliki językowe kannada dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-kn
Kannada resources for Firefox.

%description -n mozilla-firefox-lang-kn -l pl.UTF-8
Pliki językowe kannada dla Firefoksa.

%package -n mozilla-firefox-lang-ko
Summary:	Korean resources for Firefox
Summary(pl.UTF-8):	Koreańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ko
Korean resources for Firefox.

%description -n mozilla-firefox-lang-ko -l pl.UTF-8
Koreańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ku
Summary:	Kurdish resources for Firefox
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ku
Kurdish resources for Firefox.

%description -n mozilla-firefox-lang-ku -l pl.UTF-8
Kurdyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lij
Summary:	Ligurian resources for Firefox
Summary(pl.UTF-8):	Liguryjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lij
Ligurian resources for Firefox.

%description -n mozilla-firefox-lang-lij -l pl.UTF-8
Liguryjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lt
Summary:	Lithuanian resources for Firefox
Summary(pl.UTF-8):	Litewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lt
Lithuanian resources for Firefox.

%description -n mozilla-firefox-lang-lt -l pl.UTF-8
Litewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-lv
Summary:	Latvian resources for Firefox
Summary(pl.UTF-8):	Łotewskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-lv
Latvian resources for Firefox.

%description -n mozilla-firefox-lang-lv -l pl.UTF-8
Łotewskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-mai
Summary:	Maithili resources for Firefox
Summary(pl.UTF-8):	Pliki językowe maithili dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mai
Maithili resources for Firefox.

%description -n mozilla-firefox-lang-mai -l pl.UTF-8
Pliki językowe maithili dla Firefoksa.

%package -n mozilla-firefox-lang-mk
Summary:	Macedonian resources for Firefox
Summary(pl.UTF-8):	Macedońskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mk
Macedonian resources for Firefox.

%description -n mozilla-firefox-lang-mk -l pl.UTF-8
Macedońskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ml
Summary:	Malayalam resources for Firefox
Summary(pl.UTF-8):	Pliki językowe malajalam dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ml
Malayalam resources for Firefox.

%description -n mozilla-firefox-lang-ml -l pl.UTF-8
Pliki językowe malajalam dla Firefoksa.

%package -n mozilla-firefox-lang-mr
Summary:	Marathi resources for Firefox
Summary(pl.UTF-8):	Pliki językowe marathi dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-mr
Marathi resources for Firefox.

%description -n mozilla-firefox-lang-mr -l pl.UTF-8
Pliki językowe marathi dla Firefoksa.

%package -n mozilla-firefox-lang-ms
Summary:	Malay resources for Firefox
Summary(pl.UTF-8):	Malajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ms
Malay resources for Firefox.

%description -n mozilla-firefox-lang-ms -l pl.UTF-8
Malajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nb
Summary:	Norwegian Bokmaal resources for Firefox
Summary(pl.UTF-8):	Norweskie (bokmaal) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nb
Norwegian Bokmaal resources for Firefox.

%description -n mozilla-firefox-lang-nb -l pl.UTF-8
Norweskie (bokmaal) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nl
Summary:	Dutch resources for Firefox
Summary(pl.UTF-8):	Holenderskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nl
Dutch resources for Firefox.

%description -n mozilla-firefox-lang-nl -l pl.UTF-8
Holenderskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-nn
Summary:	Norwegian Nynorsk resources for Firefox
Summary(pl.UTF-8):	Norweskie (nynorsk) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-nn
Norwegian Nynorsk resources for Firefox.

%description -n mozilla-firefox-lang-nn -l pl.UTF-8
Norweskie (nynorsk) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-or
Summary:	Oriya resources for Firefox
Summary(pl.UTF-8):	Pliki językowe orija dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-or
Oriya resources for Firefox.

%description -n mozilla-firefox-lang-or -l pl.UTF-8
Pliki językowe orija dla Firefoksa.

%package -n mozilla-firefox-lang-pa
Summary:	Panjabi resources for Firefox
Summary(pl.UTF-8):	Pendżabskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pa
Panjabi resources for Firefox.

%description -n mozilla-firefox-lang-pa -l pl.UTF-8
Pendżabskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pl
Summary:	Polish resources for Firefox
Summary(pl.UTF-8):	Polskie pliki językowe dla Firefoksa
Group:		I18n
URL:		http://www.firefox.pl/
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pl
Polish resources for Firefox.

%description -n mozilla-firefox-lang-pl -l pl.UTF-8
Polskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt_BR
Summary:	Portuguese (Brazil) resources for Firefox
Summary(pl.UTF-8):	Portugalskie (brazylijskie) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt_BR
Portuguese (Brazil) resources for Firefox.

%description -n mozilla-firefox-lang-pt_BR -l pl.UTF-8
Portugalskie (brazylijskie) pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-pt
Summary:	Portuguese (Portugal) resources for Firefox
Summary(pl.UTF-8):	Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-pt
Portuguese (Portugal) resources for Firefox.

%description -n mozilla-firefox-lang-pt -l pl.UTF-8
Portugalskie pliki językowe dla Firefoksa (wersja dla Portugalii).

%package -n mozilla-firefox-lang-rm
Summary:	Romansh resources for Firefox
Summary(pl.UTF-8):	Retoromańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-rm
Romansh resources for Firefox.

%description -n mozilla-firefox-lang-rm -l pl.UTF-8
Retoromańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ro
Summary:	Romanian resources for Firefox
Summary(pl.UTF-8):	Rumuńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ro
Romanian resources for Firefox.

%description -n mozilla-firefox-lang-ro -l pl.UTF-8
Rumuńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ru
Summary:	Russian resources for Firefox
Summary(pl.UTF-8):	Rosyjskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ru
Russian resources for Firefox.

%description -n mozilla-firefox-lang-ru -l pl.UTF-8
Rosyjskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-si
Summary:	Sinhala resources for Firefox
Summary(pl.UTF-8):	Syngaleskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-si
Sinhala resources for Firefox.

%description -n mozilla-firefox-lang-si -l pl.UTF-8
Syngaleskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sk
Summary:	Slovak resources for Firefox
Summary(pl.UTF-8):	Słowackie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sk
Slovak resources for Firefox.

%description -n mozilla-firefox-lang-sk -l pl.UTF-8
Słowackie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sl
Summary:	Slovene resources for Firefox
Summary(pl.UTF-8):	Słoweńskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sl
Slovene resources for Firefox.

%description -n mozilla-firefox-lang-sl -l pl.UTF-8
Słoweńskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-son
Summary:	Songhai resources for Firefox
Summary(pl.UTF-8):	Songhajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-son
Songhai resources for Firefox.

%description -n mozilla-firefox-lang-son -l pl.UTF-8
Songhajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sq
Summary:	Albanian resources for Firefox
Summary(pl.UTF-8):	Albańskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sq
Albanian resources for Firefox.

%description -n mozilla-firefox-lang-sq -l pl.UTF-8
Albańskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sr
Summary:	Serbian resources for Firefox
Summary(pl.UTF-8):	Serbskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sr
Serbian resources for Firefox.

%description -n mozilla-firefox-lang-sr -l pl.UTF-8
Serbskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-sv
Summary:	Swedish resources for Firefox
Summary(pl.UTF-8):	Szwedzkie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-sv
Swedish resources for Firefox.

%description -n mozilla-firefox-lang-sv -l pl.UTF-8
Szwedzkie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-ta
Summary:	Tamil (India) resources for Firefox
Summary(pl.UTF-8):	Tamilskie pliki językowe dla Firefoksa (wersja dla Indii)
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-ta
Tamil (India) resources for Firefox.

%description -n mozilla-firefox-lang-ta -l pl.UTF-8
Tamilskie pliki językowe dla Firefoksa (wersja dla Indii).

%package -n mozilla-firefox-lang-te
Summary:	Telugu resources for Firefox
Summary(pl.UTF-8):	Pliki językowe telugu dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-te
Telugu resources for Firefox.

%description -n mozilla-firefox-lang-te -l pl.UTF-8
Pliki językowe telugu dla Firefoksa.

%package -n mozilla-firefox-lang-th
Summary:	Thai resources for Firefox
Summary(pl.UTF-8):	Tajskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-th
Thai resources for Firefox.

%description -n mozilla-firefox-lang-th -l pl.UTF-8
Tajskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-tr
Summary:	Turkish resources for Firefox
Summary(pl.UTF-8):	Tureckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-tr
Turkish resources for Firefox.

%description -n mozilla-firefox-lang-tr -l pl.UTF-8
Tureckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-uk
Summary:	Ukrainian resources for Firefox
Summary(pl.UTF-8):	Ukraińskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-uk
Ukrainian resources for Firefox.

%description -n mozilla-firefox-lang-uk -l pl.UTF-8
Ukraińskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-uz
Summary:	Uzbek resources for Firefox
Summary(pl.UTF-8):	Uzbeckie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-uz
Uzbek resources for Firefox.

%description -n mozilla-firefox-lang-uz -l pl.UTF-8
Uzbeckie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-vi
Summary:	Vietmanese resources for Firefox
Summary(pl.UTF-8):	Wietnamskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-vi
Vietmanese resources for Firefox.

%description -n mozilla-firefox-lang-vi -l pl.UTF-8
Wietnamskie pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-xh
Summary:	Xhosa resources for Firefox
Summary(pl.UTF-8):	Pliki językowe xhosa dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-xh
Xhosa resources for Firefox.

%description -n mozilla-firefox-lang-xh -l pl.UTF-8
Pliki językowe xhosa dla Firefoksa.

%package -n mozilla-firefox-lang-zh_CN
Summary:	Simplified Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie (uproszczone) pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_CN
Simplified Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_CN -l pl.UTF-8
Chińskie uproszczone pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zh_TW
Summary:	Traditional Chinese resources for Firefox
Summary(pl.UTF-8):	Chińskie tradycyjne pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zh_TW
Traditional Chinese resources for Firefox.

%description -n mozilla-firefox-lang-zh_TW -l pl.UTF-8
Chińskie tradycyjne pliki językowe dla Firefoksa.

%package -n mozilla-firefox-lang-zu
Summary:	Zulu resources for Firefox
Summary(pl.UTF-8):	Zuluskie pliki językowe dla Firefoksa
Group:		I18n
Requires:	iceweasel >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}

%description -n mozilla-firefox-lang-zu
Zulu resources for Firefox.

%description -n mozilla-firefox-lang-zu -l pl.UTF-8
Zuluskie pliki językowe dla Firefoksa.

%prep
unpack() {
    local args="$1" file="$2"
	local lang=$(basename $file .xpi)
	install -d $lang
	cd $lang
	cp -p $file .
	cd ..
}
%define __unzip unpack
%setup -qcT %(seq -f '-a %g' 0 88 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{firefoxdir}/extensions
for a in */*.xpi; do
	basename=$(basename $a .xpi)
	cp -p $a $RPM_BUILD_ROOT%{firefoxdir}/extensions/langpack-$basename@firefox.mozilla.org.xpi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -n mozilla-firefox-lang-ach
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ach@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-af
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-af@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-an
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-an@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ar
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ar@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-as
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-as@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ast
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ast@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-az
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-az@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-be
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-be@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bg
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bg@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-BD@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bn_IN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bn-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-br
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-br@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-bs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-bs@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ca
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ca@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cs
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cs@firefox.mozilla.org.xpi

#%files -n mozilla-firefox-lang-csb
#%defattr(644,root,root,755)
#%{firefoxdir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-de@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-dsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-dsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-el
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-el@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_GB
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-GB@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_US
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-US@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-en_ZA
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-en-ZA@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eo
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eo@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_AR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-AR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_CL
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-CL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-ES@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-es_MX
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-es-MX@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-et
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-et@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-eu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-eu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fa@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ff
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ff@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-fy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-fy-NL@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ga
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ga-IE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gd
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gd@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-gu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-gu-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-he
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-he@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hi-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hsb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hsb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hu@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-hy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-hy-AM@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-id
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-id@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-is
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-is@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-it
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-it@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ja
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ja@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-km
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-km@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-kn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-kn@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ko
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ko@firefox.mozilla.org.xpi

#%files -n mozilla-firefox-lang-ku
#%defattr(644,root,root,755)
#%{firefoxdir}/extensions/langpack-ku@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lij
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lij@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lt@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-lv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-lv@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mai
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mai@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ml
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ml@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-mr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-mr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ms
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ms@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nb-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-nn
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-nn-NO@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-or
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-or@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pa
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pa-IN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt_BR
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-BR@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-pt
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-pt-PT@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-rm
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-rm@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ro
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ro@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ru
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ru@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-si
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-si@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sl
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sl@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-son
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-son@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sq
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sq@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-sv
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-sv-SE@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-ta
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ta@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-te
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-te@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-th
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-th@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-tr
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-tr@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-uk
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-uk@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-uz
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-uz@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-vi
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-vi@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-xh
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-xh@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_CN
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-CN@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-zh_TW
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zh-TW@firefox.mozilla.org.xpi

#%files -n mozilla-firefox-lang-zu
#%defattr(644,root,root,755)
#%{firefoxdir}/extensions/langpack-zu@firefox.mozilla.org.xpi
