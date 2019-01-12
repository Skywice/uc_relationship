import re

html_content = r'''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <!--world higherlist-->
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>China-US - China Daily - Opinion - Chinadaily.com.cn</title>
    <meta name="Keywords" />
    <meta name="Description" />

    <link rel="stylesheet" type="text/css" href="//img2.chinadaily.com.cn/static/2017www_world_page_en/css/layout.css?t=655" />

    <link rel="stylesheet" type="text/css" href="//img2.chinadaily.com.cn/static/2017www_world_page_en/css/r-column.css" />
  <link rel="stylesheet" type="text/css" href="//img2.chinadaily.com.cn/static/2017www_world_page_en/css/r-public.css?var=123" />

    <link rel="stylesheet" type="text/css" href="//img2.chinadaily.com.cn/static/2017www_world_page_en/css/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="//img2.chinadaily.com.cn/static/2017www_world_page_en/css/world.css?var=112" />
 <script xml:space="preserve" src="//img2.chinadaily.com.cn/static/common/js/html5shiv.js"></script>
<script xml:space="preserve" src="//img2.chinadaily.com.cn/static/common/js/respond.min.js"></script>
  <link href="//img2.chinadaily.com.cn/h5hack/respond-proxy.html" id="respond-proxy" rel="respond-proxy" />
 <link href="/h5hack/respond.proxy.gif" id="respond-redirect" rel="respond-redirect" />
<script src="/h5hack/respond.proxy.js" xml:space="preserve"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <script language="javascript" type="text/javascript" xml:space="preserve" src="//img2.chinadaily.com.cn/static/2017www_world_page_en/js/koala.min.1.5.js"></script><!--焦点图-->

    <script language="javascript" type="text/javascript" xml:space="preserve" src="//img2.chinadaily.com.cn/static/2017www_world_page_en/js/jquery-1.10.2.js"></script><!--jquery-->
    <script language="javascript" type="text/javascript" xml:space="preserve" src="//img2.chinadaily.com.cn/static/2017www_world_page_en/js/bootstrap.min.js"></script><!-- bootstrap js -->
    <script language="javascript" type="text/javascript" xml:space="preserve" src="//img2.chinadaily.com.cn/static/2017www_world_page_en/js/tabs.js"></script>
    <!--[if lt IE 9]>
    <style type="text/css">
        .swipe-p{
            background:transparent;
            filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#66000000,endColorstr=#66000000);
            zoom: 1;
        }
        .zhezhao{
            background-color:#ddd;
        }
    </style>
    <![endif]-->
    
      <META name="filetype" content="1" />
      <META name="publishedtype" content="1" />
      <META name="pagetype" content="2" />
      <meta name="catalogs" content="59b8d011a3108c54ed7dfc54" />
    
</head>
<body>
<!-- 公共头部开始 -->

      <!-- begin响应式遮罩层-->
      <div class="zhezhao"></div>
      <!-- end 响应式遮罩 -->
      <!-- 响应式nav开始 -->
      <nav class="navbartop1">
        <div class="nav-fluid">
          <div class="yinyingceng"></div>
          <button type="button" class="navbutton1 res-m">
            <span class="icon-bar1"></span>
            <span class="icon-bar1"></span>
            <span class="icon-bar1"></span>
          </button>
        </div>
        <div class="img-center res-m">
          <a class="a-center" target="_top" href="//www.chinadaily.com.cn"><img src="//www.chinadaily.com.cn/image_e/2017/logo.png" alt="chinadaily" />
          </a>
        </div>
        <div class="fl-right res-m">
          <a href="//cn.chinadaily.com.cn" target="_top"><img src="//www.chinadaily.com.cn/image_e/2017/cnbut.png" /></a>
        </div>
      </nav>
      <!-- 响应式nav结束 -->
      <ul class="xiao-ul">
        <li><a href="//newssearch.chinadaily.com.cn/en/search" target="_top"><span>Search</span></a></li>
        <li><a target="_top" href="//www.chinadaily.com.cn">HOME</a></li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/china">CHINA</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/world">WORLD</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/business">BUSINESS</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/life">LIFESTYLE</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/culture">CULTURE</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/travel">TRAVEL</a>
          </li>
        <li><a href="http://watchthis.chinadaily.com.cn" target="_blank">WATCHTHIS</a></li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/sports">SPORTS</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/opinion">OPINION</a>
          </li>
        <li>
          <a target="_top" href="//www.chinadaily.com.cn/regional">REGIONAL</a>
          </li>
        <li><a href="http://bbs.chinadaily.com.cn/" target="_top">FORUM</a></li>
        <li><a href="javascript:void(0)">NEWSPAPER</a></li>
        <li><a href="//www.chinadaily.com.cn/newmedia.html" target="_top">MOBILE</a></li>
      </ul>
      <!-- pc头部 -->
      <div class="topBar">
        <div class="logo"><a target="_top" href="//www.chinadaily.com.cn"><img src="//www.chinadaily.com.cn/image_e/2016/logo_art.jpg" /></a></div>
        <div class="search">
          <form name="searchform" method="get" action="//newssearch.chinadaily.com.cn/en/search" onsubmit="return do_search(this)" target="_blank">
            <input name="query" id="searchText" onfocus="cleanword(this)" type="text" />
            <span><img src="//www.chinadaily.com.cn/image_e/2016/fdj_art.gif" onclick="javascript:searchform.submit()" /></span>
          </form>
        </div>
        <div class="channel">
          <span><a href="//global.chinadaily.com.cn" target="_blank">Global Edition</a><a href="http://www.chinadailyasia.com/" target="_blank">ASIA</a></span>
          <span><a href="http://cn.chinadaily.com.cn" target="_blank">中文</a><a href="http://language.chinadaily.com.cn" target="_blank">双语</a><a href="http://www.chinadaily.com.cn/chinawatch_fr/index.html" target="_blank">Français</a></span>
        </div>
        <div class="topInfo"><a href="http://bbs.chinadaily.com.cn/member.php?mod=register.php" target="_blank" style="padding-right: 28px;"><img src="//www.chinadaily.com.cn/image_e/2016/sign_ico_art.gif" /></a><a href="http://subscription.chinadaily.com.cn/" target="_blank"><img src="//www.chinadaily.com.cn/image_e/2016/sub_ico_art.gif" /></a></div>
      </div>
      <!-- pc 菜单 -->
      <div class="topNav">
        <ul class="dropdown">
          <li style="width: 55px;"><a target="_top" href="//www.chinadaily.com.cn">HOME</a></li>
          <li style=" width:55px;">
            <a target="_top" href="//www.chinadaily.com.cn/china">CHINA</a>
            </li>
          <li style=" width:65px;">
            <a target="_top" href="//www.chinadaily.com.cn/world">WORLD</a>
            </li>
          <li style=" width:75px;">
            <a target="_top" href="//www.chinadaily.com.cn/business">BUSINESS</a>
            </li>
          <li style=" width:75px;">
            <a target="_top" href="//www.chinadaily.com.cn/life">LIFESTYLE</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/culture">CULTURE</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/travel">TRAVEL</a>
            </li>
          <li style=" width:75px;"><a href="//watchthis.chinadaily.com.cn" target="_blank">WATCHTHIS</a></li>
          <li style=" width:65px;">
            <a target="_top" href="//www.chinadaily.com.cn/sports">SPORTS</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/opinion">OPINION</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/regional">REGIONAL</a>
            </li>
          <li style=" width:75px;"><a href="http://bbs.chinadaily.com.cn/" target="_blank">FORUM</a></li>
          <li class="newspaper"><a href="javascript:void(0);">NEWSPAPER</a>
            <ul class="sub_menu">
              <li><a href="http://newspress.chinadaily.net.cn" target="_blank" style="width:110px;">China Daily PDF</a></li>
              <li><a href="http://www.chinadaily.com.cn/cndy/index1.html" target="_top" style="width:130px;">China Daily E-paper</a></li>
            </ul>
          </li>
          <li style="width:75px;"><a href="https://www.chinadaily.com.cn/newmedia.html" target="_blank">MOBILE</a></li>
        </ul>
      </div>
    
<!-- 公共头部结束 -->
<!-- pc 二级菜单 -->
<div class="topNav2_art"> <span>World</span>
    <ul>
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/asia_pacific">Asia-Pacific</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/america">Americas</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/europe">Europe</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/middle_east">Middle East</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/africa">Africa</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/china-us">China-US</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/cn_eu">China-Europe</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/China-Japan-Relations">China-Japan</a></li>
        
        
            <li><a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/china-africa">China-Africa</a></li>
        
    </ul>
</div>
<!-- 响应式二级菜单 -->
<ol class="breadcrumb res-m" id="bread-nav1">
 
        
            
                <li><a shape="rect" href="//www.chinadaily.com.cn">Home</a></li>
                
                
            
        
 
        
            
                
                
                <li><a shape="rect" href="//www.chinadaily.com.cn/world">World</a></li>
            
        
 
        
            
                
                / China-US
                
            
        
   
</ol>

<!-- pc 当前栏目 -->
<div class="topNav3_art"> <span id="bread-nav">
    
      
        <a shape="rect" href="//www.chinadaily.com.cn">Home</a>
        
        
      
    
    
      
        
        <a shape="rect" href="//www.chinadaily.com.cn/world">/ World</a>
        
      
    
    
      
        
        
        <a shape="rect" href="//www.chinadaily.com.cn/world/china-us">/ China-US</a>
      
    
  </span> </div>
<div class="main_art">
    <div class="lft_art" id="left">
        <div class="tw2" style="margin-bottom:10px;">
            <div class="tw2_l">
                
                    
                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37cfaea3106c65c34e3c9e.html"><img width="290" height="187" src="//img2.chinadaily.com.cn/images/201901/11/5c37ef86a3106c65fff4a240.jpeg" /></a>
                        <span class="tw2_l_t"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37cfaea3106c65c34e3c9e.html">Sino-US teamwork urged for managing differences</a></span>
                    
                    
                
            </div>
            <div class="tw2_r">
                <div class="mb10">
                    
                        
                            <div class="tBox2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c379647a3106c65c34e3c78.html">Talks calm trade climate for Beijing, Washington</a></div>
                        
                        
                            <div class="tBox2" style="margin-right:0px;"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c34bb88a31068606745f8bf.html">Cui: China-US relations a success story</a></div>
                        
                    
                </div>
                <div>
                    
                        
                        
                        
                            <div class="tBox2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c33c39aa31068606745f579.html">Bank of China Chicago seeks to localize operation in US</a></div>
                        
                        
                            <div class="tBox2" style="margin-right:0px;"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c3375d1a31068606745f55d.html">Chinese companies at electronics show seek more cooperation</a></div>
                        
                    
                </div>
            </div>
        </div>

        <!--list-->
        
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/12/WS5c38db2fa3106c65c34e3ffa.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/12/5c38db2fa3106c65fff4d7b2.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/12/WS5c38db2fa3106c65c34e3ffa.html">China Daily USA publishes <EM>Chinese Enterprises in the United States 2019</EM></a></h4>
                <b>2019-01-12 02:06</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/12/WS5c38cb4ca3106c65c34e3ff6.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/12/5c38cc12a3106c65fff4d714.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/12/WS5c38cb4ca3106c65c34e3ff6.html">Gansu students' visit with NBA's Spurs is an amazing show of friendship and sportsmanship</a></h4>
                <b>2019-01-12 00:58</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/11/5c38b543a3106c65fff4d628.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38b543a3106c65c34e3feb.html">Pompeo promotes 'reinvigorated' US role in Middle East</a></h4>
                <b>2019-01-11 23:24</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38b25fa3106c65c34e3fe5.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/11/5c38b25fa3106c65fff4d5fe.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38b25fa3106c65c34e3fe5.html">Trade issue won't stop wave of China's tech innovation</a></h4>
                <b>2019-01-11 23:12</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38ae0da3106c65c34e3fde.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/12/5c38c1f7a3106c65fff4d689.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c38ae0da3106c65c34e3fde.html">Autonomous driving’s optimism on display at CES</a></h4>
                <b>2019-01-11 22:54</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37855fa3106c65c34e3c69.html">Former administrator of NASA applauded Chang’e moon far side landing</a></h4>
                <b>2019-01-11 01:48</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c3696a9a3106c65c34e394f.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/10/5c36b7b9a3106c65fff47da3.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c3696a9a3106c65c34e394f.html">China, US agree to keep close contact after trade talks</a></h4>
                <b>2019-01-10 08:23</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c36898fa3106c65c34e391a.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/10/5c36b847a3106c65fff47f35.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c36898fa3106c65c34e391a.html">Tesla factory points to appeal of China market</a></h4>
                <b>2019-01-10 07:53</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c36431da3106c65c34e38a7.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/10/5c36431da3106c65fff45edc.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c36431da3106c65c34e38a7.html">US stocks trade higher on China-US trade optimism</a></h4>
                <b>2019-01-10 02:53</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c34beffa31068606745f8c2.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/08/5c34beffa310686029df1301.png" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c34beffa31068606745f8c2.html">Louisiana celebrates its prosperous trade with China</a></h4>
                <b>2019-01-08 23:17</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c34145ba31068606745f77a.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/08/5c34145ba310686029df01be.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c34145ba31068606745f77a.html">Philadelphia New Year celebration highlights traditional Chinese culture</a></h4>
                <b>2019-01-08 11:09</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c3385bca31068606745f568.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/08/5c3385bca310686029dee824.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/08/WS5c3385bca31068606745f568.html">Tesla breaks ground on gigafactory in Shanghai</a></h4>
                <b>2019-01-08 01:00</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c3373bfa31068606745f55a.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/07/5c3373bfa310686029dee79c.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c3373bfa31068606745f55a.html">Brookings' China Center director sees exchange of ideas as key benefit of reform</a></h4>
                <b>2019-01-07 23:43</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c32c8cca31068606745f401.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/07/5c32c8cca310686029decf52.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c32c8cca31068606745f401.html">Onemile launches worldwide scooter rental project</a></h4>
                <b>2019-01-07 11:34</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c300111a31068606745f015.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/05/5c302023a310686029de95e4.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c300111a31068606745f015.html">China rejects claims of travel risks made by US in advisory to citizens</a></h4>
                <b>2019-01-05 08:57</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2fae70a31068606745efbc.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/05/5c2fe3fca310686029de905b.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2fae70a31068606745efbc.html">Dem says Trump threatened 'years' for shutdown</a></h4>
                <b>2019-01-05 03:05</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2facfba31068606745efb8.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/05/5c2facfba310686029de8f85.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2facfba31068606745efb8.html">US soybeans higher following trade talks announcement</a></h4>
                <b>2019-01-05 02:59</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2f9fcda31068606745efa8.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/05/5c2fe2cda310686029de8fdb.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/05/WS5c2f9fcda31068606745efa8.html">High-level trade talks with US to start</a></h4>
                <b>2019-01-05 02:02</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/04/WS5c2f750ca31068606745ef98.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/04/5c2f750ca310686029de8e7c.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/04/WS5c2f750ca31068606745ef98.html">Trump targeting Asian immigrants</a></h4>
                <b>2019-01-04 23:00</b>
              </span>
                </div>
            
            
                <div class="mb10 tw3_01_2 ">
                    

                        <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/04/WS5c2f5a42a31068606745ef86.html">
                            <img width="200" height="130" src="//img2.chinadaily.com.cn/images/201901/04/5c2f67b5a310686029de8e57.jpeg" />
                        </a>

                    
                    <span class="tw3_01_2_t">
                <h4><a shape="rect" href="//www.chinadaily.com.cn/a/201901/04/WS5c2f5a42a31068606745ef86.html">China refutes US travel advice</a></h4>
                <b>2019-01-04 21:06</b>
              </span>
                </div>
            

            <!-- pc 分页 -->
            <div id="div_currpage">
                
      
        
        

        <!--up-->
        
          
            
            <span style="background-color: #003366;color: #fff;">1</span>
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_2.html">2</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_3.html">3</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_4.html">4</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_5.html">5</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_6.html">6</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_7.html">7</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_8.html">8</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_9.html">9</a>
            
          
        
        
          
            <a href="//www.chinadaily.com.cn/world/china-us/page_10.html">10</a>
            
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        
          
        
        <!--down-->
        <a class="pagestyle" href="//www.chinadaily.com.cn/world/china-us/page_2.html">Next</a>&nbsp;&nbsp;
        <a style="text-decoration:none" href="//www.chinadaily.com.cn/world/china-us/page_113.html">&gt;&gt;|</a>
      
    
            </div>
            <!-- pc 分页结束 -->

            <!-- 响应式分页 -->
            <div class="selectpage">
                <!--移动分页-->
                
              
                    <span class="pageno">
                <a href="javascript:void (0)" shape="rect">
                  1/113</a>
              </span>
                    <span class="next">
                <a class="pagestyle" shape="rect" href="//www.chinadaily.com.cn/world/china-us/page_2.html">Next</a>
              </span>
                
            </div>
            <!-- 响应式分页结束 -->





    </div>
    <div class="mai_r">
        <div class="bt2" style="margin-bottom:5px;"> <b><a href="#" shape="rect">Most Viewed in 24 Hours</a></b></div>
        <script src="//www.chinadaily.com.cn/html/topnews/59b8d00fa3108c54ed7dfc04.js" xml:space="preserve"></script>
        <script xml:space="preserve">
            /*<![CDATA[*/
            var num;
            document.write('<ul class=\"lisBox\">');
            for(var i=0;i<5;i++){
                num=i+1;
                document.write('<li><a href="'+cd_json[i].url+'" target="_blank">'+cd_json[i].title+'</a></li>');
            }
            document.write('</ul>');
            /*]]>*/
        </script>
       <!--Special-->
        <div class="bt2">
            <b>
                
                    <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/special_coverage">Special Coverage</a>
                    <span><a shape="rect" href="//www.chinadaily.com.cn/world/special_coverage">+</a></span>
                
            </b>
        </div>
      <div class="tw4Box">
            
                
                    <div class="tw4">
                        <div class="tw4_p"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201811/27/WS5bfc9708a310eff30328b2db.html"><img width="140" height="90" src="//img2.chinadaily.com.cn/images/201811/27/5bfc9708a310eff3690836d6.jpeg" /></a></div>
                        <div class="tw4_t"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201811/27/WS5bfc9708a310eff30328b2db.html">Xi visits Europe and S. America, attends G20 Summit</a></div>
                    </div>

                
                
                    <div class="tw4">
                        <div class="tw4_p"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201811/14/WS5bebbd71a310eff303288a93.html"><img width="140" height="90" src="//img2.chinadaily.com.cn/images/201811/14/5bebbe00a310eff369064268.jpeg" /></a></div>
                        <div class="tw4_t"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201811/14/WS5bebbd71a310eff303288a93.html">Xi visits Oceania and SE Asia, attends APEC meeting</a></div>
                    </div>

                

        </div>
        <!--welly photo-->
        <div class="bt2">
            <b>
                
                    <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/world-in-photos">World in photos</a>
                    
                
            </b>
        </div>
        <div class="tw8">
            
                
              <span>
                <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c32c218a31068606745f3c9.html">
                  <img width="290" height="187" src="//img2.chinadaily.com.cn/images/201901/07/5c32c320a310686029decdac.jpeg" />
                </a>
              </span>
                    <span class="tw8_t"><a shape="rect" href="//www.chinadaily.com.cn/a/201901/07/WS5c32c218a31068606745f3c9.html">The world in photos: Dec 31 - Jan 6</a></span>
                
            
        </div>
        <!--Newsmaker-->
          <div class="bt2">
            <b>
                
                    <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/newsmaker">Newsmakers</a>
                    <span><a shape="rect" href="//www.chinadaily.com.cn/world/newsmaker">+</a></span>
                
            </b>
        </div>
        <div class="tw4Box">
            
                
                    <div class="tw4">
                        <div class="tw4_p"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c375da6a3106c65c34e3c57.html"><img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/11/5c37e063a3106c65fff49bd2.jpeg" /></a></div>
                        <div class="tw4_t"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c375da6a3106c65c34e3c57.html">Divorce could knock Jeff Bezos out of world's richest spot</a></div>
                    </div>

                
                
                    <div class="tw4">
                        <div class="tw4_p"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37fb19a3106c65c34e3e1b.html"><img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/11/5c37fb19a3106c65fff4a777.jpeg" /></a></div>
                        <div class="tw4_t"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37fb19a3106c65c34e3e1b.html">2018 has seen fear of warming planet</a></div>
                    </div>

                

        </div>
        
    
        <div style="clear:both">

        </div>
        <div class="mb20">
            <div class="tw6Box_2" style="margin-right:10px;">
                <!--China-Japan-->
                <div class="bt2">
                    <b>
                        
                            <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/China-Japan-Relations">China-Japan Relations</a>
                            
                        
                    </b>
                </div>
                
                    
                        <div class="tw6_2">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201812/26/WS5c2350cfa310d9121405112a.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201812/26/5c2350cfa310d9126fdb969b.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201812/26/WS5c2350cfa310d9121405112a.html">New book on Kyoto released by Shanghai publisher</a></span>
                        </div>
                    
                    
                        <div class="tw6_2" style="margin-bottom:0px;">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201812/13/WS5c11bb06a310eff303290c0a.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201812/13/5c11bb06a310eff3690ab2af.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201812/13/WS5c11bb06a310eff303290c0a.html">Japanese civil groups mark 81st anniversary of Nanjing Massacre</a></span>
                        </div>
                    
                
            </div>
            <div class="tw6Box_2">
                <!--China-US-->
                <div class="bt2">
                    <b>
                        
                            <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/china-us">China-US</a>
                            
                        
                    </b>
                </div>
                
                    
                        <div class="tw6_2">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37cfaea3106c65c34e3c9e.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/11/5c37ef86a3106c65fff4a240.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37cfaea3106c65c34e3c9e.html">Sino-US teamwork urged for managing differences</a></span>
                        </div>
                    
                    
                        <div class="tw6_2" style="margin-bottom:0px;">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c379647a3106c65c34e3c78.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/11/5c37ec44a3106c65fff4a027.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c379647a3106c65c34e3c78.html">Talks calm trade climate for Beijing, Washington</a></span>
                        </div>
                    
                
            </div>
        </div>
        <div class="mb20">
            <div class="tw6Box_2" style="margin-right:10px;">
                <!--China-Europe-->
                <div class="bt2">
                    <b>
                        
                            <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/cn_eu">China-Europe</a>
                            
                        
                    </b>
                </div>
                
                    
                        <div class="tw6_2">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37f518a3106c65c34e3dcc.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/11/5c37f518a3106c65fff4a4b9.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/11/WS5c37f518a3106c65c34e3dcc.html">China, France to launch joint projects under B&R Initiative: ambassador</a></span>
                        </div>
                    
                    
                        <div class="tw6_2" style="margin-bottom:0px;">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c3702efa3106c65c34e3bfe.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/10/5c3709dfa3106c65fff48b21.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/10/WS5c3702efa3106c65c34e3bfe.html">China-Russia bilateral trade surpasses $100b record high</a></span>
                        </div>
                    
                
            </div>
            <div class="tw6Box_2">
                <!--China-Africa-->
                <div class="bt2">
                    <b>
                        
                            <a target="_top" shape="rect" href="//www.chinadaily.com.cn/world/china-africa">China-Africa</a>
                            
                        
                    </b>
                </div>
                
                    
                        <div class="tw6_2">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/09/WS5c35327ca31068606745f90b.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/09/5c35327ca310686029df16ed.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/09/WS5c35327ca31068606745f90b.html">Archaeologists dig deep on overseas projects</a></span>
                        </div>
                    
                    
                        <div class="tw6_2" style="margin-bottom:0px;">
                  <span class="tw6_p2">
                    <a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/09/WS5c353745a31068606745f92d.html">
                      <img width="140" height="90" src="//img2.chinadaily.com.cn/images/201901/09/5c354a64a310686029df1df7.jpeg" />
                    </a>
                  </span>
                            <span class="tw6_t2"><a target="_blank" shape="rect" href="//www.chinadaily.com.cn/a/201901/09/WS5c353745a31068606745f92d.html">40 years of Djibouti ties hailed</a></span>
                        </div>
                    
                
            </div>
        </div>
        <!--div class="ad1"> <img src="img/ad1.jpg" width="290" height="120" /></div-->
    </div>
</div>
<!-- 响应式回顶部 -->
<!-- 公共尾部开始 -->

      <!-- 响应式回顶部 -->
      <div data-am-widget="gotop" class="am-gotop am-gotop-fixed WIDGET-58db5c3d3f6a4d70c2315464 gotop am-no-layout am-active res-m">
        <span class="am-gotop-title">Top</span>
        <i class="am-gotop-icon am-icon-arrow-up gotop"></i>
      </div>
      <!-- 响应式回顶部结束 -->
      <!--pc回顶部-->
      <div class="hui-dingbu">
        <div class="ding-nei"><a href="">BACK TO THE TOP</a></div>
      </div>
      <!--底部-->
      <div class="dibu-one"></div>
      <!--底部2-->
      <div class="topNav_art2">
        <ul class="dropdown" style="width:1010px; margin:0 auto;">
          <li style="width: 50px;"><a target="_top" href="//www.chinadaily.com.cn">HOME</a></li>
          <li style=" width:55px;">
            <a target="_top" href="//www.chinadaily.com.cn/china">CHINA</a>
            </li>
          <li style=" width:65px;">
            <a target="_top" href="//www.chinadaily.com.cn/world">WORLD</a>
            </li>
          <li style=" width:80px;">
            <a target="_top" href="//www.chinadaily.com.cn/business">BUSINESS</a>
            </li>
          <li style=" width:80px;">
            <a target="_top" href="//www.chinadaily.com.cn/life">LIFESTYLE</a>
            </li>
          <li style=" width:65px;">
            <a target="_top" href="//www.chinadaily.com.cn/culture">CULTURE</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/travel">TRAVEL</a>
            </li>
          <li style=" width:75px;"><a href="http://watchthis.chinadaily.com.cn" target="_top">WATCHTHIS</a></li>
          <li style=" width:60px;">
            <a target="_top" href="//www.chinadaily.com.cn/sports">SPORTS</a>
            </li>
          <li style=" width:70px;">
            <a target="_top" href="//www.chinadaily.com.cn/opinion">OPINION</a>
            </li>
          <li style=" width:65px;">
            <a target="_top" href="//www.chinadaily.com.cn/regional">REGIONAL</a>
            </li>
          <li style=" width:68px;"><a href="http://bbs.chinadaily.com.cn/" target="_top">FORUM</a></li>
          <li class="newspaper"><a href="javascript:void(0);">NEWSPAPER</a>
            <ul class="sub_menu">
              <li><a href="http://newspress.chinadaily.net.cn" target="_blank" style="width:110px;">China Daily PDF</a></li>
              <li><a href="http://www.chinadaily.com.cn/cndy/index1.html" atremote="1" target="_top" style="width:130px;">China Daily E-paper</a></li>
            </ul>
          </li>
          <li><a href="//www.chinadaily.com.cn/newmedia.html" target="_top" atremote="1">MOBILE</a></li>
        </ul>
      </div>
      <!--底部3-->
      <div class="dibu-three">
        <div class="dibu-three-nei">
          <div class="three-left">
            <div class="lo-g"><a target="_top" atremote="1" href="//www.chinadaily.com.cn"><img src="//www.chinadaily.com.cn/image_e/2016/sub/a-1.jpg" /></a></div>

            <div class="lo-a">Copyright 1995 - <script>
              //<![CDATA[
              var oTime = new Date();
              document.write(oTime.getFullYear());
              //]]>
              </script> . All rights reserved. The content (including but not limited to text, photo, multimedia information, etc) published in this site belongs to China Daily Information Co (CDIC). Without written authorization from CDIC, such content shall not be republished or used in any form. Note: Browsers with 1024*768 or higher resolution are suggested for this site.</div>

            <div class="lo-c"><span style="display:none;">License for publishing multimedia online <b><a href="//www.chinadaily.com.cn/2009image_e/permit2010.jpg" target="_blank" atremote="1">0108263</a></b></span><br />
              <br />
              Registration Number: 130349 <img src="//www.chinadaily.com.cn/image_e/2016/sub/a-2.jpg" /></div>
          </div>

          <div class="three-midd">
            <div class="midd-a"><a href="//www.chinadaily.com.cn/e/static_e/about" target="_top">About China Daily</a></div>

            <div class="midd-a"><a href="//www.chinadaily.com.cn/e/static_e/advertiseonsite" target="_top">Advertise on Site</a></div>

            <div class="midd-a"><a href="//www.chinadaily.com.cn/e/static_e/contact" target="_top">Contact Us</a></div>

            <div class="midd-a"><a href="http://chinadaily.zhiye.com/" target="_blank">Job Offer</a></div>

            <div class="midd-a"><a href="//www.chinadaily.com.cn/static_e/Expat_Employment.html" target="_blank">Expat Employment</a></div>
          </div>

          <div class="three-right">
            <div class="right-a">FOLLOW US</div>

            <div class="right-b"><span><a href="http://www.facebook.com/chinadaily" target="_blank"><img src="//www.chinadaily.com.cn/image_e/2016/sub/a-3.jpg" border="0" /></a></span> 

              <span><a href="https://twitter.com/ChinaDailyUSA" target="_blank"><img src="//www.chinadaily.com.cn/image_e/2016/sub/a-4.jpg" atremote="1" border="0" /></a></span></div>
          </div>
        </div>
      </div>
      <!-- 响应式foot -->
      <footer class="mobile-foot">
        <div class="mobile-miscs res-m">
          <p>
            <span class="footer-eng">English</span><span class="footer-driver">|</span><span class="footer-chin"><a href="//cn.chinadaily.com.cn">中文</a></span>
          </p>
          <p class="footer-p">
            Copyright 1995 - <script>
            //<![CDATA[
            var oTime = new Date();
            document.write(oTime.getFullYear());
            //]]>
            </script> . All rights reserved. The content (including but not limited to text, photo, multimedia information, etc) published in this site belongs to China Daily Information Co (CDIC). Without written authorization from CDIC, such content shall not be republished or used in any form.
          </p>
        </div>
      </footer>
      <!-- 响应式foot 结束-->
    
<!-- 公共尾部结束 -->
<script xml:space="preserve" src="//img2.chinadaily.com.cn/static/2017www_world_page_en/js/swipe.js"></script>
<script type="text/javascript" xml:space="preserve">

    var bullets = document.getElementById('position').getElementsByTagName('li');
    var banner = Swipe(document.getElementById('mySwipe'), {
        auto: 2000,
        continuous: true,
        disableScroll:false,
        callback: function(pos) {
            var i = bullets.length;
            while (i--) {
                bullets[i].className = ' ';
            }
            bullets[pos].className = 'cur';
        }
    });
</script>
<!--<script type="text/javascript">-->
<!--$(window).scroll(function(){-->

<!--if($(window).scrollTop()>100 && $("html").width()<600){-->
<!--$(".gotop").fadeIn(100);-->
<!--}else{-->
<!--$(".gotop").fadeOut(100);-->
<!--}-->
<!--})-->
<!--$(".gotop").click(function(){-->
<!--$('html,body').animate({scrollTop:0},300);-->
<!--})-->

<!--</script>-->
<!--<script type="text/javascript">-->
<!--$(".yinyingceng").click(function(){-->
<!--$('#xialacaidan').collapse('hide')-->
<!--$(".xiao-ul").animate({left:'0px'},"slow");-->
<!--$(".xiao-ul").hide().css("display","block");-->
<!--$(".zhezhao").show().css({height:$("html").height()});-->

<!--})-->
<!--$(".zhezhao").click(function(){-->

<!--$(".xiao-ul").animate({left:'-500px'},"slow");-->
<!--$(".zhezhao").hide().css("display","none");-->


<!--})-->
<!--</script>-->
<style type="text/css" xml:space="preserve">
    .lf{
        width: 695px;
    }
</style>

      <div style="display:none">
        <script type="text/javascript">
          //<![CDATA[
          document.write(unescape("%3Cscript src='//cl2.webterren.com/webdig.js?z=16' type='text/javascript'%3E%3C/script%3E"));
          //]]>
        </script>
        <script type="text/javascript">
          //<![CDATA[
          wd_paramtracker("_wdxid=000000000000000000000000000000000000000000")
          //]]>
        </script>
      </div>
    

      <div style="display:none;">
     <script src="//s13.cnzz.com/stat.php?id=3089622&amp;web_id=3089622" language="JavaScript"></script>
        <!-- Start Alexa Certify Javascript -->
        <script type="text/javascript">
          //<![CDATA[
          _atrk_opts = { atrk_acct:"uM+9j1a8Dy00qn", domain:"chinadaily.com.cn",dynamic: true};
          (function() { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://certify-js.alexametrics.com/atrk.js"; var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as, s); })();
          //]]>
        </script>
        <noscript><img src="https://certify.alexametrics.com/atrk.gif?account=uM+9j1a8Dy00qn" style="display:none" height="1" width="1" alt="" /></noscript>
        <!-- End Alexa Certify Javascript -->  
      </div>

    
</body>
</html>
'''

re_content = r'''<h4><a shape="rect" href="(.*?)">(.*?)</a></h4>\n\s*<b>(.*?)</b>'''
pattern = re.compile(re_content, re.DOTALL)
a = re.findall(pattern, html_content)
for i in a:
    print(i)