//请求国家
request_get('http://www.beejeen.com/POICountry',append_country_list);

//请求城市
$('#country_list').on('change',function(){
	request_get('http://www.beejeen.com/POICity?key='+encodeURIComponent($(this).val()),append_city_list);
});

//选择上传图片还是视频
$('#check-img').on('click',function(){
	$('.image-box').show();
	$('.video-box').hide();
});
$('#check-video').on('click',function(){
	$('.video-box').show();
	$('.image-box').hide();
});

//增加上传的图片
$('#add').on('click',function(){
	$('<div><input class="image-upload" type="file" /></div>').insertBefore('#add');
});


//提交数据
$('#submit').on('click',function(){
	var data = new FormData();
	data.append( 'country' , $('#country_list').val() );
	data.append( 'city' , $('#city_list').val() );
	data.append( 'name' , $('#name').val() );
	data.append( 'intro', $('#intro').val() );
//	服务
	var service = [];
	$('input[name="service"]:checked').each(function(){
		service.push( $(this).val() );
	});
	data.append( 'service', service.join(',') );
//	缩略图
	data.append('thumb',  $('#thumb')[0].files[0] );
//	媒体类型
	data.append('media_type', $('input[name="media"]:checked').val() );
	if( $('input[name="media"]:checked').val()==0 ){
		//	图片
		var imgs = [];
		$('.image-upload').each(function(){
			imgs.push( this.files[0] );
		});
		console.log(imgs);
		data.append('img',  imgs );
		//	音乐
		data.append('music', $('#music')[0].files[0] );
	}else{
		//	视频
		data.append('video', $('#video')[0].files[0] );
	}

	$.ajax({
            type: "POST",
            enctype: 'multipart/form-data',
            url: "http://www.beejeen.com/uploadPOI?type="+ $('input[name="type"]:checked').val(),
            data: data,
            processData: false,
            contentType: false,
            cache: false,
            timeout: 5000,
            success: function(data){
                console.log(data);
            },
            error: function(e){
                console.log(e);
            }
    });
    
});

function request_get( url , callback ){
    $.ajax({
	    url:url,
	    type:'get',
	    async:true,
	    timeout:5000,
	    dataType:'json',
	    beforeSend:function(xhr){
	        console.log(xhr)
	        console.log('发送前')
	    },
	    success:function(data,textStatus,jqXHR){
	        console.log('成功')
	        console.log(data)
	        console.log(textStatus)
	        console.log(jqXHR)
			callback(data);
	    },
	    error:function(xhr,textStatus){
	        console.log('错误')
	        console.log(xhr)
	        console.log(textStatus)
	    },
	    complete:function(){
	        console.log('结束')
	    }
  	});
}

function append_country_list( data ){

	var str = '';

	for( var i=0; i < data.country.length ; i++ ){
		str += '<option>' + data.country[i] + '</option>';
	}

	$('#country_list').html(str);
}


function append_city_list( data ){

	var str = '';

	for( var i=0; i < data.city.length ; i++ ){
		str += '<option>' + data.city[i] + '</option>';
	}

	$('#city_list').html(str);
}
