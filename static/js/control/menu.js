(function (window, document) {

    var layout   = document.getElementById('layout'),
        menu     = document.getElementById('menu'),
        menuLink = document.getElementById('menuLink');

    function toggleClass(element, className) {
        var classes = element.className.split(/\s+/),
            length = classes.length,
            i = 0;

        for(; i < length; i++) {
          if (classes[i] === className) {
            classes.splice(i, 1);
            break;
          }
        }
        // The className is not found
        if (length === classes.length) {
            classes.push(className);
        }

        element.className = classes.join(' ');
    }

    menuLink.onclick = function (e) {
        var active = 'pure-menu-selected';

        e.preventDefault();
        console.log('toggling');
        toggleClass(layout, active);
        toggleClass(menu, active);
        toggleClass(menuLink, active);
    };

    menuLink.onclick(function(e){
        e.preventDefault();
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

}(this, this.document));