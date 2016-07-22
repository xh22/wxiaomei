    $(document).ready(function() {
		$('#calendar').fullCalendar({

            minTime: '10:30:00', // a start time (10am in this example)
            maxTime: '19:00:00', // an end time (6pm in this example)
            slotDuration: "00:10:00",
            allDaySlot: false,
            lang: 'zh-cn',
			header: {
				left: 'prev,next today',
				center: 'title',
				//right: 'agendaDay,agendaWeek,month',
				right: ''
			},
            timezone: 'local',
            defaultView:'agendaWeek',
            selectOverlap: false,
            eventStartEditable: false,
            eventDurationEditable: false,
            selectable: false,
			//select: function(start, end) {
            eventClick: function(event, jsEvent, view) {        
                $('#subscribewrap').attr("style", "");            
                $("#subscribewrap").dialog({
                    title:    "预约类型:"+event.type+" 预约时间:"+new Date(event.start).toLocaleString()+"--"+new Date(event.end).toLocaleString()
                  , 'class':  "mydialog"  /*add custom class for this dialog*/
                  , onClose: function() { $(this).dialog("close"); }
                  , buttons: [
                      {
                          text: "获取验证码"
                        , 'class': "btn-success"
                        , click: function() {
                            /*your login handler*/
                            if (event.title[event.title.length-1]<1){
                                alert("预约人数已满，请选择其他时间!")
                                return false;
                            };
                            var reg = /^0?1[3|4|5|8][0-9]\d{8}$/;
                            if (!reg.test($("#phonenum").val())) {
                                alert("请填写合法手机号!");
                                return false;
                            };
                            var i=1; 
                            var t = $(".btn-success");
                            t.attr('disabled',true); 
                            var timer=setInterval(function(){t.text((60-i)+"秒后重新获取");i++;
                            if(i>59){t.attr('disabled',false);i=1;t.text("获取验证码");clearInterval(timer)}},1000) 

                            $.ajax({
                                type: 'POST',
                                url: '/verify/msg',
                                data: {
                                    // our hypothetical feed requires UNIX timestamps
							        phonenum: $("#phonenum").val()
                                },
                                success:function(msg) {  
                                    alert("验证码已发送!");  
                                },  
                                error:function() {  
                                    alert("请稍后再试!");  
                                },  
                     
                            });
                          }
                      },
                      {
                          text: "预约"
                        , classed: "btn-error"  /*classed equal to 'class'*/
                        , click: function() {
                            /*your login handler*/
                              $.ajax({
                                  type: 'POST',
                                  url: '/subscribe/calendar',
                                  data: {
                                      // our hypothetical feed requires UNIX timestamps
                                      start: event.start.unix(),
                                      end: event.end.unix(),
							          verifycode: $("#code").val(),
							          phonenum: $("#phonenum").val(),
							          name: $("#name").val()
                                  },
                                  success:function(msg) {  
							          //$('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
                                      alert("预约成功!");  
                                  },  
                                  error:function() {  
                                      alert("验证码错误!");  
                                  },  
    
                              });
                              $(this).dialog("close");
                          }
                      }
                    ]
                });
                

//				var title = confirm("是否预约此时间段?");
				$('#calendar').fullCalendar('unselect');
			},
			editable: true,
			eventLimit: true, // allow "more" link when too many events
            events: function(start, end, timezone, callback) {
                $.ajax({
                    url: '/subscribe/calendar',
                    type: 'GET',
                    data: {
                    },
                    success: function(doc) {
                        var events = [];
                        doc = JSON.parse(doc),
                        $.each(doc['event'],function(n, value) {
                            events.push({
                                title: "余额"+(3-value[2].split(",").length),
                                start: new Date((value[0])*1000), // will be parsed
                                end: new Date((value[1])*1000), // will be parsed
                                type: doc['type'],
                            });
                        });
                        callback(events);
                    }
                });
            }
		});
		
	});
