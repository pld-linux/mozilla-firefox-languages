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
Version:	29.0.1
Release:	1
License:	MPL v2.0
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ach.xpi
# Source0-md5:	c96c9cbf85c35282cc7652ab79882674
Source1:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/af.xpi
# Source1-md5:	b2022f355b600a96d2d171dd9eed76d5
Source2:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/an.xpi
# Source2-md5:	675eabbd40744d1a032ab3984a0770b1
Source3:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ar.xpi
# Source3-md5:	cc546e1fd570ca47d28a76eb0ce3a4aa
Source4:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/as.xpi
# Source4-md5:	5ffdcecb12689baf8fa3c16834d60578
Source5:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ast.xpi
# Source5-md5:	a5263f2e715549dc63ba74fede853ec9
Source6:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/be.xpi
# Source6-md5:	af6ef1d6f4f7bf94e09c7a1e293ad905
Source7:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bg.xpi
# Source7-md5:	e62c365c7222c89b06133f5028157d90
Source8:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-BD.xpi
# Source8-md5:	553b721c4794b437ab8840b7e98cffa5
Source9:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bn-IN.xpi
# Source9-md5:	de55cd3b8d46ef47731e2bc44de3b7f2
Source10:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/br.xpi
# Source10-md5:	78b930cf109cf916759e3ee98dcc3af5
Source11:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/bs.xpi
# Source11-md5:	889b666680748fbf65dac8108f8b7c94
Source12:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source12-md5:	12509a01285cf06409017a26b17c3375
Source13:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cs.xpi
# Source13-md5:	36f867bc95a7f174bcf77b4b548f9c6a
Source14:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/csb.xpi
# Source14-md5:	02747ea5caffe9578ccc476137d5c5be
Source15:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/cy.xpi
# Source15-md5:	1a63a511d4ae3faa9f0671b7775de14b
Source16:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/da.xpi
# Source16-md5:	b2ff658fe32ecb09f6062e7ed3b62931
Source17:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/de.xpi
# Source17-md5:	acc96484100af138cf1b6a0b06b68ac0
Source18:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/el.xpi
# Source18-md5:	a004df7f38ab7888feef22481feca599
Source19:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-GB.xpi
# Source19-md5:	768d5e6e7e6b92ae3d5efcc4be8e3616
Source20:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-US.xpi
# Source20-md5:	eed6e7b836360a4eeb70a929ff66e010
Source21:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/en-ZA.xpi
# Source21-md5:	6c44369dcc754f72ab7f00c7a395ac89
Source22:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eo.xpi
# Source22-md5:	3e3033494fa133a6132215c75a26051c
Source23:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-AR.xpi
# Source23-md5:	72d80266631d8fefadee8a8f5830ec70
Source24:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-CL.xpi
# Source24-md5:	1f5ae0c989166c717551c9884d5c9516
Source25:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-ES.xpi
# Source25-md5:	ca49ba9a7d421d2db581a8e38dd528b5
Source26:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/es-MX.xpi
# Source26-md5:	f4b8309d646047e1323e46a493f3b8ac
Source27:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/et.xpi
# Source27-md5:	5a066d6160be55c0e15e9a5d71877068
Source28:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/eu.xpi
# Source28-md5:	c80c246127a1f7509d59e46fcd60d9ce
Source29:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fa.xpi
# Source29-md5:	9e81d58c29382835e9a74f09db1ecd13
Source30:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ff.xpi
# Source30-md5:	a01c5d921b4856c8469ee0ac5041851e
Source31:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fi.xpi
# Source31-md5:	3c5b91d68edd902a7297b024ea4e174f
Source32:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fr.xpi
# Source32-md5:	6afb7cb4d60cb20fa12bd893ed4b2bfd
Source33:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/fy-NL.xpi
# Source33-md5:	2e4a97ef5302ce19bcaad369216ebf30
Source34:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ga-IE.xpi
# Source34-md5:	0466c7d0891b44b585c4dc5415fc73db
Source35:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gd.xpi
# Source35-md5:	0a1cf404d5c83543cbca9a05c618deae
Source36:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gl.xpi
# Source36-md5:	d295da51ce0a4887820f164dd526f06a
Source37:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/gu-IN.xpi
# Source37-md5:	1e63090d0ca33be7f2f5dcd0380063ce
Source38:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/he.xpi
# Source38-md5:	2650a3fc5a37e4debf58afc2345a79c4
Source39:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hi-IN.xpi
# Source39-md5:	ad1465700197dd4a23d7f31adf41123f
Source40:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hr.xpi
# Source40-md5:	cdafe8db84b382e24d2684adf0dbb6d3
Source41:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hu.xpi
# Source41-md5:	fe84ba127d1a6e2177c19ee3711fa8ec
Source42:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/hy-AM.xpi
# Source42-md5:	4453b9dc9d022e712da7d5ccec0da631
Source43:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/id.xpi
# Source43-md5:	273442f1e9e8c211353d0e2a22b185d2
Source44:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/is.xpi
# Source44-md5:	d04f6cc9a95d4ffdfc9f83ae225efa82
Source45:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/it.xpi
# Source45-md5:	d7d3eb177c8218c8910276e5f514657a
Source46:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ja.xpi
# Source46-md5:	a1e21484e61f1feab83a4cbfe743bd99
Source47:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kk.xpi
# Source47-md5:	3a3dca089fe77da6cc5cf342b2fc7337
Source48:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/km.xpi
# Source48-md5:	c2409801888459d685a978bab57a4e13
Source49:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/kn.xpi
# Source49-md5:	d743e7d7ca283c6f056e5475195cf7a4
Source50:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ko.xpi
# Source50-md5:	369ba48e3c8dc1e384945db5f6a8e867
Source51:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ku.xpi
# Source51-md5:	47f8826030abca2bffb4d06c755f5663
Source52:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lij.xpi
# Source52-md5:	3442a27583b497464b51ff3990dd9a43
Source53:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lt.xpi
# Source53-md5:	eaf4a3381395ef6bf1962a4b502ccbd6
Source54:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/lv.xpi
# Source54-md5:	82c1207e8dabf593b404e037bcbb792f
Source55:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mai.xpi
# Source55-md5:	8a68a7aff5cc17d38ee5ffe655cd77c2
Source56:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mk.xpi
# Source56-md5:	732946faeb5fae1b63ff3b6ecbdc182a
Source57:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ml.xpi
# Source57-md5:	eb84f4ced9308faf70302edfebcdbe7e
Source58:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/mr.xpi
# Source58-md5:	7f3c0132acf073ea373be4533d500423
Source59:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ms.xpi
# Source59-md5:	74e3c26b55688d205c2a6557e5e9a1cb
Source60:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nb-NO.xpi
# Source60-md5:	bcf452d3561bf56b277f422f80163650
Source61:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nl.xpi
# Source61-md5:	77ba5065d618c91b03db34f5c0a723f2
Source62:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/nn-NO.xpi
# Source62-md5:	7616a8e101639f720825135a8f059738
Source63:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/or.xpi
# Source63-md5:	9f8892c66b1bb32dc9601d1b6a085bf0
Source64:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pa-IN.xpi
# Source64-md5:	d30bc708247e6492b018fedbeb89989e
Source65:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pl.xpi
# Source65-md5:	e91cd800528e3e9b9628c03affb646da
Source66:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-BR.xpi
# Source66-md5:	a3f60cd08f71386f9f6260189983630a
Source67:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/pt-PT.xpi
# Source67-md5:	54c328aa2f34414db954186b8536c214
Source68:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/rm.xpi
# Source68-md5:	8282b134a7f149afcad78f02f1c5ac6f
Source69:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ro.xpi
# Source69-md5:	b550f414e2fa51824a6c05ccd5d7faef
Source70:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ru.xpi
# Source70-md5:	017f952d116613f4b30269787c134654
Source71:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/si.xpi
# Source71-md5:	e9868ce409a57c45331b86d9b21d49bb
Source72:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sk.xpi
# Source72-md5:	bc34c1db51d88da0e89016833973cc42
Source73:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sl.xpi
# Source73-md5:	fb650e36e9251ec13d7477bc1f1769a0
Source74:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/son.xpi
# Source74-md5:	dd04dcde064b7152de4f3d03d782f6bb
Source75:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sq.xpi
# Source75-md5:	70ab64262f70a9ac163777ca6735c148
Source76:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sr.xpi
# Source76-md5:	84f04f1385ff2c44c51146322e4a3d88
Source77:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/sv-SE.xpi
# Source77-md5:	0f859796856c2df12a8ae6ddb1433ff4
Source78:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ta.xpi
# Source78-md5:	3acf512b415ea857add48df7fec35e6d
Source79:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/te.xpi
# Source79-md5:	e7ba9d310eca019eec6643f5d0a61cf1
Source80:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/th.xpi
# Source80-md5:	4a1fd83238d436070aeb783132b3e6a8
Source81:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/tr.xpi
# Source81-md5:	088293d4089da69e57030230147d2224
Source82:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/uk.xpi
# Source82-md5:	9745edf6893a7e78a8fa888374c807e0
Source83:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/vi.xpi
# Source83-md5:	1bc1d409edb2cffcde707a0c43016618
Source84:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/xh.xpi
# Source84-md5:	acab242bdcfa1f50dec54e6808852b2b
Source85:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-CN.xpi
# Source85-md5:	6baa90870c2f6d695c834c0dd2ed7144
Source86:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zh-TW.xpi
# Source86-md5:	ddd6c1e5b908370c753dbe84737951a7
Source87:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/zu.xpi
# Source87-md5:	b4543ad3f44c235b237ff7ea7838a4e6
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
%setup -qcT %(seq -f '-a %g' 0 87 | xargs)

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

%files -n mozilla-firefox-lang-csb
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-csb@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-cy
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-cy@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-da
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-da@firefox.mozilla.org.xpi

%files -n mozilla-firefox-lang-de
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-de@firefox.mozilla.org.xpi

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

%files -n mozilla-firefox-lang-ku
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-ku@firefox.mozilla.org.xpi

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

%files -n mozilla-firefox-lang-zu
%defattr(644,root,root,755)
%{firefoxdir}/extensions/langpack-zu@firefox.mozilla.org.xpi
