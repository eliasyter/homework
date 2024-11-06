
document.addEventListener("DOMContentLoaded", function() {
    // Hent dagens dato
    const today = new Date();

    // Hent alle radene i tabellen
    const rows = document.querySelectorAll("table tr");

    rows.forEach(row => {
        // Hent fristdatoen fra første kolonne i raden
        const fristCell = row.querySelector("td:first-child");
        if (!fristCell) return;

        const fristDate = new Date(fristCell.textContent);

        // Beregn antall dager til fristen
        const diffTime = fristDate - today;
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

        // Legg til CSS-klasse basert på antall dager til fristen
        if (diffDays > 7) {
            // Mer enn 7 dager igjen, sett til grønn
            fristCell.textContent= `${diffDays} dager`
            row.classList.add("frisk");
        } else if (diffDays > 3) {
            fristCell.textContent= `${diffDays} dager`
            // Mindre enn 7 dager, men fortsatt tid igjen, sett til gul
            row.classList.add("snart");
        } else {
            // Fristen er passert eller i dag, sett til rød
            row.classList.add("overfrist");
            fristCell.textContent= `${diffDays} dager`
        }
    });
});

