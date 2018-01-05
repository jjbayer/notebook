$(document).ready(function() {


    var converter = new showdown.Converter();
    converter.setFlavor('github');

    $('.note-content').each(function(i, x) {
        var el = $(x)
        el.html(converter.makeHtml(el.text()))
    })

    $('#notes').on('click', 'a.edit-note', function(e) {
        e.preventDefault()
        var noteSelector = '.note'
        var noteClass = 'edit-mode'
        var note = $(this).closest(noteSelector)
        note.siblings(noteSelector).removeClass(noteClass)
        note.toggleClass(noteClass)
    })

    // ace.edit('new-note')


    // text      = '#hello, markdown!',
    // html      = converter.makeHtml(text);

})