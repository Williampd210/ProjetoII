document.addEventListener('DOMContentLoaded', function () {
    // Definindo o mês e ano atuais
    const dataAtual = new Date();
    const ano = dataAtual.getFullYear();
    const mes = dataAtual.getMonth();

    // Função para gerar o calendário
    function gerarCalendario(ano, mes) {
        const primeiroDiaDoMes = new Date(ano, mes, 1);
        const ultimoDiaDoMes = new Date(ano, mes + 1, 0);
        const diasNoMes = ultimoDiaDoMes.getDate();

        // Selecionando o elemento do calendário
        const calendarioMes = document.getElementById('calendario-mes');
        calendarioMes.innerHTML = ''; // Limpa o conteúdo anterior

        // Adicionando os dias do mês
        for (let dia = 1; dia <= diasNoMes; dia++) {
            const diaElement = document.createElement('div');
            diaElement.classList.add('dia');
            diaElement.textContent = dia;

            // Verificando se existe um agendamento para esse dia
            if (agendamentos[dia]) {
                diaElement.classList.add('agendado');
            }

            calendarioMes.appendChild(diaElement);
        }
    }

    // Exemplo de agendamentos TROCAR PELA BASE DE DADOS
    const agendamentos = {
        5: [{ nome: 'Joaquina', horario: '10:00', data: '05/02/2025' }],
        10: [{ nome: 'Joaquina2', horario: '14:00', data: '10/02/2025' }],
        15: [{ nome: 'Joaquina3', horario: '19:00', data: '15/02/2025' }],
        20: [{ nome: 'Joaquina4', horario: '09:00', data: '20/02/2025' }],
        25: [{ nome: 'Joaquina5', horario: '16:00', data: '25/02/2025' }],
    };

    // Função para gerar a lista de agendamentos à esquerda
    function gerarListaAgendamentos() {
        const listaAgendamentos = document.getElementById('lista-agendamentos');
        listaAgendamentos.innerHTML = ''; // Limpa a lista anterior

        for (let dia in agendamentos) {
            agendamentos[dia].forEach(agendamento => {
                const li = document.createElement('li');
                li.textContent = `${agendamento.nome} | ${agendamento.horario} / ${agendamento.data}`;
                listaAgendamentos.appendChild(li);
            });
        }
    }

    // Gerar o calendário e a lista
    gerarCalendario(ano, mes);
    gerarListaAgendamentos();
});
