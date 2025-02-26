from config.db import get_db_connection

def obtener_reporte_dinero_recaudado(fecha_inicio, fecha_fin):
    """Obtiene el dinero recaudado en un intervalo de tiempo"""
    try:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)
        
        query = """
            SELECT id, fecha, hora_ini, hora_fin, importe
            FROM consulta
            WHERE fecha BETWEEN %s AND %s
            ORDER BY fecha ASC, hora_ini ASC
        """
        cursor.execute(query, (fecha_inicio, fecha_fin))
        resultados = cursor.fetchall()

        cursor.close()
        db.close()
        
        return resultados
    except Exception as e:
        print(f"Error al obtener el reporte: {str(e)}")
        return []
