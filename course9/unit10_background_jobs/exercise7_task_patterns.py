# Common background job patterns: emails, reports, file processing.

import asyncio
from arq import create_pool
from arq.connections import RedisSettings
import time

# Pattern 1: Send email
async def send_email_task(ctx, to: str, subject: str, body: str):
    """Send email asynchronously"""
    print(f"📧 Sending email to {to}")
    await asyncio.sleep(2)  # Simulate SMTP
    print(f"✅ Email sent: {subject}")
    return {"sent": True, "to": to}

# Pattern 2: Generate report
async def generate_report_task(ctx, user_id: int, report_type: str):
    """Generate PDF report"""
    print(f"📊 Generating {report_type} report for user {user_id}")
    await asyncio.sleep(5)  # Simulate PDF generation
    
    report_url = f"/reports/{user_id}_{report_type}.pdf"
    print(f"✅ Report generated: {report_url}")
    
    # Send email with report
    await ctx['redis'].enqueue_job(
        'send_email_task',
        f'user{user_id}@example.com',
        f'Your {report_type} report is ready',
        f'Download: {report_url}'
    )
    
    return {"report_url": report_url}

# Pattern 3: Process uploaded file
async def process_upload_task(ctx, filename: str, user_id: int):
    """Process uploaded file (resize images, etc.)"""
    print(f"🔧 Processing upload: {filename}")
    
    # Simulate processing
    await asyncio.sleep(3)
    
    processed_url = f"/processed/{filename}"
    print(f"✅ File processed: {processed_url}")
    
    # Notify user
    await ctx['redis'].enqueue_job(
        'send_email_task',
        f'user{user_id}@example.com',
        'File processed',
        f'Your file is ready: {processed_url}'
    )
    
    return {"processed_url": processed_url}

# Pattern 4: Scheduled cleanup
async def cleanup_old_files_task(ctx):
    """Run periodically to clean up old files"""
    print("🧹 Cleaning up old files")
    
    # Simulate cleanup
    await asyncio.sleep(2)
    deleted_count = 42  # Simulated
    
    print(f"✅ Deleted {deleted_count} old files")
    return {"deleted": deleted_count}

# Pattern 5: Chain tasks
async def import_data_task(ctx, csv_url: str):
    """Import data from CSV, then send summary"""
    print(f"📥 Importing data from {csv_url}")
    
    # Simulate import
    await asyncio.sleep(4)
    rows_imported = 1000
    
    print(f"✅ Imported {rows_imported} rows")
    
    # Generate report after import
    await ctx['redis'].enqueue_job(
        'generate_report_task',
        1,  # user_id
        'import_summary'
    )
    
    return {"rows_imported": rows_imported}

class WorkerSettings:
    functions = [
        send_email_task,
        generate_report_task,
        process_upload_task,
        cleanup_old_files_task,
        import_data_task
    ]
    redis_settings = RedisSettings()
    
    # Cron jobs (scheduled tasks)
    cron_jobs = [
        # Clean up old files every day at 2am
        # 'cleanup_old_files_task': {'hour': 2, 'minute': 0}
    ]

# Example usage in FastAPI
async def example_usage():
    redis = await create_pool(RedisSettings())
    
    # User signs up → send welcome email
    await redis.enqueue_job('send_email_task', 
                            'newuser@example.com',
                            'Welcome!',
                            'Thanks for joining!')
    
    # User requests report → generate in background
    await redis.enqueue_job('generate_report_task', 42, 'monthly_sales')
    
    # User uploads file → process in background
    await redis.enqueue_job('process_upload_task', 'photo.jpg', 42)
    
    # Admin imports data → chain tasks
    await redis.enqueue_job('import_data_task', 'https://example.com/data.csv')

# Run worker: arq unit10_background_jobs.exercise7_task_patterns.WorkerSettings
#
# Common patterns:
# - Emails: Always background (no one wants to wait for SMTP)
# - Reports: Background (can take minutes)
# - File processing: Background (CPU intensive)
# - Cleanup: Scheduled cron job
# - Data import: Background + chaining
