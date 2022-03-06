(() => {
  // Toastr configuration
  toastr.options.closeMethod = 'fadeOut';
  toastr.options.closeDuration = 4000;
  toastr.options.progressBar = true;
  toastr.options.rtl = true;
  toastr.options.positionClass = 'toast-bottom-right';
  toastr.options.closeButton = true;
  toastr.options.extendedTimeOut = 3000;
  toastr.options.closeEasing = 'swing';

  // Tooltips
  $('[data-toggle="tooltip"]').tooltip();

  // datepickers
  $('[data-date]').datepicker({
    rtl: true
  });
})();
