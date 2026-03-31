// ===== IPL REAL TEAM DATA =====
const IPL_TEAMS = [
  { id: 1, name: "Mumbai Indians",          short: "MI",  color: "#004BA0", city: "Mumbai" },
  { id: 2, name: "Chennai Super Kings",     short: "CSK", color: "#F9CD05", city: "Chennai" },
  { id: 3, name: "Royal Challengers Bengaluru", short: "RCB", color: "#EC1C24", city: "Bengaluru" },
  { id: 4, name: "Kolkata Knight Riders",   short: "KKR", color: "#3A225D", city: "Kolkata" },
  { id: 5, name: "Delhi Capitals",          short: "DC",  color: "#00008B", city: "Delhi" },
  { id: 6, name: "Sunrisers Hyderabad",     short: "SRH", color: "#F7A721", city: "Hyderabad" },
  { id: 7, name: "Rajasthan Royals",        short: "RR",  color: "#EA1A85", city: "Jaipur" },
  { id: 8, name: "Punjab Kings",            short: "PBKS",color: "#ED1B24", city: "Chandigarh" },
  { id: 9, name: "Lucknow Super Giants",    short: "LSG", color: "#A0E4FF", city: "Lucknow" },
  { id: 10,name: "Gujarat Titans",          short: "GT",  color: "#1C4F9C", city: "Ahmedabad" },
];

const DAY_NAMES = ["", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];

// ===== MATCH GENERATION =====
function generateMatches(teamIds) {
  const matches = [];
  for (let i = 0; i < teamIds.length; i++)
    for (let j = 0; j < teamIds.length; j++)
      if (i !== j)
        matches.push({ home: teamIds[i], away: teamIds[j] });
  return matches;
}

// ===== DAY SCHEDULING =====
function nextDay(d) { return (d % 7) + 1; }

function scheduleDays(dayOne, total, n) {
  const days = [];
  let current = dayOne;
  let i = 0;
  while (i < total) {
    days.push(current);
    if (n >= 8 && (current === 6 || current === 7) && i + 1 < total) {
      days.push(current);
      i += 2;
    } else {
      i += 1;
    }
    current = nextDay(current);
  }
  return days.slice(0, total);
}

function scheduleTime(days) {
  return days.map((day, i) => {
    if (day === 6 || day === 7) {
      if (i === 0 || days[i - 1] !== day) return "3:30 PM";
      return "7:30 PM";
    }
    return "7:30 PM";
  });
}

// ===== VENUE ASSIGNMENT =====
function assignVenues(matches, teams) {
  return matches.map(m => {
    const team = teams.find(t => t.id === m.home);
    return team ? team.city : "TBD";
  });
}

// ===== GENERATE FULL SCHEDULE =====
function generateSchedule(selectedTeamIds, dayOne) {
  const matches = generateMatches(selectedTeamIds);
  const days    = scheduleDays(dayOne, matches.length, selectedTeamIds.length);
  const times   = scheduleTime(days);
  const teams   = IPL_TEAMS.filter(t => selectedTeamIds.includes(t.id));
  const venues  = assignVenues(matches, teams);
  return { matches, days, times, venues, teams };
}

// ===== EXPORT TO CSV =====
function exportCSV(schedule) {
  const { matches, days, times, venues, teams } = schedule;
  let csv = "Match No,Day,Time,Home Team,Away Team,Venue\n";
  matches.forEach((m, i) => {
    const home = teams.find(t => t.id === m.home).name;
    const away = teams.find(t => t.id === m.away).name;
    csv += `${i+1},${DAY_NAMES[days[i]]},${times[i]},"${home}","${away}","${venues[i]}"\n`;
  });
  const blob = new Blob([csv], { type: "text/csv" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "ipl_schedule.csv";
  a.click();
}