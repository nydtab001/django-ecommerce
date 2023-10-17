const labels = document.querySelectorAll('.rating label');
//const l = document.getElementById('c-rating')

//console.log(l)

function handleSelect(selectedLabel) {
  labels.forEach((label, index) => {
    if (index <= selectedLabel) {
      label.classList.add('checked');
    } else {
      label.classList.remove('checked');
    }
  });
}

labels.forEach((label, index) => {
  label.addEventListener('click', () => {
    handleSelect(index);
  });
});

// JavaScript/jQuery
$(document).ready(function() {
    $("#sidebar").on("show.bs.collapse", function() {
        $("#chevron-down").hide();
        $("#chevron-up").show();
    });

    $("#sidebar").on("hide.bs.collapse", function() {
        $("#chevron-up").hide();
        $("#chevron-down").show();
    });
});

