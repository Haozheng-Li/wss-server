(function(document) {
    'use strict';
    let TableFilter = (function(Arr) {
        let _input;
        function _onInputEvent(e) {
            _input = e.target;
            let tables = document.getElementsByClassName(_input.getAttribute('data-table'));
            Arr.forEach.call(tables,
            function(table) {
                Arr.forEach.call(table.tBodies,
                function(tbody) {
                    Arr.forEach.call(tbody.rows, _filter);
                });
            });
        }
        function _filter(row) {
            let text = row.textContent.toLowerCase(),
            val = _input.value.toLowerCase();
            row.style.display = text.indexOf(val) === -1 ? 'none': 'table-row';
        }
        return {
            init: function() {
                let inputs = document.getElementsByClassName('table-filter');
                Arr.forEach.call(inputs,
                function(input) {
                    input.oninput = _onInputEvent;
                });
            }
        };
    })(Array.prototype);
    
    document.addEventListener('readystatechange',
    function() {
        if (document.readyState === 'complete') {
            TableFilter.init();
        }
    });
})(document);


$('#deleteDevice').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget);
    document.delete_device.action = button.data('url');
})

$(".status_change").change(function() {
    let enable_status = $(this).prop('checked');
    let action_url = $(this).data('url');
    let data_obj={'enable':enable_status};
    $.ajax({
        url:action_url,
        type:'post',
        data:data_obj,
        success:function (data) {
            let target_id = data.target_id;
            let is_enable = data.is_enable;
            let status = data.device_status;
            let target_status_node = $("#" + target_id + "_status");
            let status_inner_html = '';
            if (status === 'active'){
                status_inner_html = `<span class="badge bg-success text-uppercase">${status}</span>`
            }
            else if(status === 'inactive'){
                status_inner_html = `<span class="badge bg-warning text-uppercase">${status}</span>`
            }
            else if(status === 'inactivated'){
                status_inner_html = `<span class="badge bg-primary text-uppercase">${status}</span>`
            }
            else {
                status_inner_html = `<span class="badge bg-danger text-uppercase">${status}</span>`
            }
            target_status_node.html(status_inner_html);
        }});
});