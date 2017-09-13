
## 代码解析

1. index.html           引导及欢迎界面
2. manu-page.html       各区域图片列表展示
3. vr-player.html       全景图播放
4. auto-player.html     全景图自动旋转
5. vrshow.js            krpano引擎配置

主要数据结构:

`pageObj`
```js
var pageObj = {
        pano_id:'31',       //全景ID
        pano_json_url:'pano/listPage.json',     //全景json数据
        base_xml_url:'//data.taagoo.com/pano/base-xml.html?code=20170803363933', //基础数据
        login_id:'',
        login_url:'',
        login_avatar:'',
        is_praise:''
    };

var pageObj = {
        pano_id:'31',
        pano_json_url:'pano/data/'+request.name+'/data.json',
        base_xml_url:'//data.taagoo.com/pano/base-xml.html?code='+request.id,
        login_id:'',
        login_url:'',
        login_avatar:'',
        is_praise:''
    };
```

## 主要实现功能
1. 菜单栏实现
2. 控制栏实现
3. 导航栏实现
4. 服务器解析数据

## 插件使用

1. UtoVRPlayerGuide.js
2. 

