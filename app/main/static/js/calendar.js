    $(document).ready(function() {
		$('#calendar').fullCalendar({

            minTime: '09:00:00', // a start time (10am in this example)
            maxTime: '20:00:00', // an end time (6pm in this example)
            slotDuration: "00:20:00",
            allDaySlot: false,
            lang: 'zh-cn',
			header: {
				left: 'prev,next today',
				center: 'title',
				//right: 'agendaDay,agendaWeek,month',
				right: 'agendaDay'
			},
            timezone: 'UTC',
            defaultView:'agendaDay',
			selectable: true,
			selectHelper: true,
			select: function(start, end) {
				var title = confirm("是否预约此时间段?");
				var eventData;
				if (title) {
					eventData = {
						start: start,
						end: end
					};
                    $.ajax({
                        type: 'POST',
                        url: '/subscribe/calendar',
                        data: {
                            // our hypothetical feed requires UNIX timestamps
                            start: start.unix(),
                            end: end.unix(),
                        },
                        success:function(msg) {  
					        $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
                            alert("预约成功!");  
                        },  
                        error:function() {  
                            alert("请稍后再试!");  
                        },  

                    });
				}
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
                                title: value[2],
                                start: new Date(value[0]*1000), // will be parsed
                                end: new Date(value[1]*1000), // will be parsed
                            });
                        });
                        callback(events);
                    }
                });
            }
		});
		
	});
