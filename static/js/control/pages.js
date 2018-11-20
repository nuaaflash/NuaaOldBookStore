$(document).ready(function() {
    // 改变类
    function changeClassFrom(element, className, oldclassName) {
        debugger;
        var classes = element.className.split(/\s+/),
            length = classes.length,
            i = 0;

        // 删除旧className
        for(; i < length; i++) {
          if (classes[i] === oldclassName) {
            classes.splice(i, 1);
            break;
          }
        }
        
        // 加入新className
        classes.push(className);

        element.className = classes.join(' ');
        console.log(element.className);
    }

    function showTheForms() {
        var pop = document.getElementById('popup');
        var back_of_pop = document.getElementById('backgroud_popup');
        pop.style.display = "block";
        back_of_pop.style.display = "block";
    }

    // 提交结果
    function submitResult() {
        var pop = document.getElementById('popup');
        var back_of_pop = document.getElementById('backgroud_popup');
        console.log($scope);
        //创建对象
        console.log(sjob)
        var worker = {"flag":false,"worker_id":worker_id,"job":sjob,"detail":detail,"done":done,"review":review};
        //放进数组
        workers.push(worker);
        pop.style.display = "none";
        back_of_pop.style.display = "none";
    }

    // 关闭弹窗
    function closePop(){
        var pop = document.getElementById('popup');
        var back_of_pop = document.getElementById('backgroud_popup');
        pop.style.display = "none";
        back_of_pop.style.display = "none";
    }

    $("div.selectButton").click(function(){
        // class被换掉前获取当前被选中的button
        selectOne = $("div.sideButtonSelected")[0];

        var thisOneIsNotSelected = false;
        classes = $(this)[0].className.split(/\s+/)
        for(i in classes){
            if('sideButton' ===  classes[i]){
                thisOneIsNotSelected = true;
            }
        }

        if(thisOneIsNotSelected){
            changeClassFrom($(this)[0],'sideButtonSelected','sideButton');
            changeClassFrom($(this)[0].childNodes[3],'sideButtonLabelSelected','sideButtonLabel');
            debugger;
        }
        
        debugger;
        if(selectOne.id != $(this)[0].id){
            changeClassFrom(selectOne,'sideButton','sideButtonSelected');
            changeClassFrom(selectOne.childNodes[3],'sideButtonLabel','sideButtonLabelSelected');
        }
        debugger;  
      });


    $('button#add-a-book').on('click', function() { 
            event.preventDefault();
            showTheForms();
    });

    $('button#comfire-add-a-book').on('click', function() { 
            event.preventDefault();
            submitResult();
    });

    $('button#cancle-add-a-book').on('click', function() { 
            event.preventDefault();
            closePop();
    });
});
